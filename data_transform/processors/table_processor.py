import pandas as pd



class TableProcessor:
    def __init__(self, variables):
        self.variables = variables

    def process(self, df):
        df = (df
            .pipe(self._add_workplace_columns)
     #       .pipe(self._date_format)
            .pipe(self._map_columns)
            .pipe(self._rename_columns)
            .pipe(self._column_ordering)
             )

        return df

    def _date_format(self, df):
        date_column_name = self.variables.DATE_COLUMNS[0]
        df[date_column_name] = df[date_column_name].dt.strftime('%d.%m.%Y %H:%M:%S')
       
        return df
        
    def _column_ordering(self, df):
        df_columns = set(df.columns)
        export_columns = set(self.variables.COLUMNS_ORDER)
        
        if export_columns.intersection(df_columns) != export_columns:
            raise ValueError('Columns are different.')

        df = df[self.variables.COLUMNS_ORDER]

        return df

    
    def _rename_columns(self, df):
        df.rename(columns=self.variables.RENAMED_COLUMNS, inplace=True)
        return df
    
    def _add_workplace_columns(self, df):
        captor_data = pd.DataFrame(self.variables.TABLE_DATA)
        df = df.merge(captor_data, how='cross')
        return df

    def _map_columns(self, df):
        for new, from_col in self.variables.COLUMN_MAPPER.items():
            df[new] = df[from_col]
        return df