from data_transform.variables import Variables
from data_transform.csv_loader import CSVLoader
from data_transform.processors.lnr_processor import LNRProcessor
from data_transform.processors.table_processor import TableProcessor
import os

if __name__ == '__main__':
    import_path = os.path.join('exports')
    export_path = os.path.join('xlsx')
    file_name = 'export.xlsx'
    configs = Variables()
    
    csv_loader = CSVLoader(configs)
    processor = LNRProcessor(configs)
    captor_table = TableProcessor(configs)
    
    row_df = csv_loader.load_csv(path=import_path)
    finished_df = processor.process(row_df)
    export_df = captor_table.process(finished_df)
    csv_loader.export(export_df, path=export_path, file_name=file_name)
    print('end')