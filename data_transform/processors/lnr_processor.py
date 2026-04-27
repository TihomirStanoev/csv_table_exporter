import numpy as np
import pandas as pd


class LNRProcessor:
    def __init__(self, variables):
        self.variables = variables
        self.t06 = pd.to_datetime('06:00:00').time()
        self.t14 = pd.to_datetime('14:00:00').time()
        self.t22 = pd.to_datetime('22:00:00').time()
        self.t00 = pd.to_datetime('00:00:00').time()
        
    def process(self, df):
        df = (df
            .pipe(self._replace_colum)
            .pipe(self._merge_dfs)
            .pipe(self._calculate_pieces)
            .pipe(self._return_s3_date)
            .pipe(self._shifts)
            .pipe(self._group_by_date)
             )

        return df

    def _group_by_date(self, df):
        df = df.groupby(self.variables.GROUPBY_COLUMNS)[self.variables.SUM_COLUMNS].sum().reset_index()
        return df
    

    def _replace_colum(self, df):
        df['Detail'] = df['Detail'].replace('RA', 'TYPE_20372')
        return df

    def _merge_dfs(self, df):
        captor_mapping = pd.DataFrame(self.variables.TABLE_MAPPING)
        df = df.merge(captor_mapping, left_on='Detail', right_on='Detail', how='inner')
        return df

    def _calculate_pieces(self, df):        
        df['goodQuantity'] = np.where(df['Result'] == 'IO', 1, 0)
        df['badQuantity'] =  np.where(df['Result'] != 'IO', 1, 0)
        df['totalQuantity'] = df['goodQuantity']  + df['badQuantity']
        return df


    def _return_s3_date(self, df):
        date_col = pd.to_datetime(df['Date']).dt.date
        time_col = pd.to_datetime(df['Time']).dt.time
        pervius_date = date_col - pd.Timedelta(1, 'D')

        condition = (time_col >= self.t00) & (time_col < self.t06)
        
        df['Date'] = np.where(condition, pervius_date, date_col)

        return df
        
    
    def _shifts(self, df):
        time_col = df['Time'].dt.time
        
        choices = ['S1', 'S2']
        conditions = [
                (time_col >= self.t06) & (time_col < self.t14),
                (time_col >= self.t14) & (time_col < self.t22),
            ]
        
        df['Shift'] = np.select(conditions, choices, default='S3')

        return df