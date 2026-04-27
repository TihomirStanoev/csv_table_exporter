from config import TABLE_MAPPING, TABLE_DATA, SHEET_NAME


class Variables:
    NEEDED_COLUMNS = [
        'AssociationId', 
        'Date', 
        'Time', 
        'Result', 
        'Detail',
        'Routing card',
    ]

    REMOVE_DUPLICATES = [
        'AssociationId',
        'Date', 
        'Time',
    ]

    INVALID_ASSOCIATION_ID = [0,-1]
    
    RENAMED_COLUMNS = {
        'Date': 'Aggrupation period'}
    
    COLUMNS_TYPES = {
        'AssociationId': 'Int64',
        'Result': 'str', 
        'Detail': 'str',
        'Routing card':'str'}
    
    DATE_COLUMNS = [
        'Date',
        'Time'
    ]
    
    TABLE_MAPPING = TABLE_MAPPING

    COLUMN_MAPPER = {
        'Order name': 'Manufacturing reference name',}
    
    TABLE_DATA = TABLE_DATA

    GROUPBY_COLUMNS = [
        'Date', 
        'Manufacturing reference', 
        'Manufacturing reference name', 
        'Shift'
    ]
    
    SUM_COLUMNS = [
        'goodQuantity', 
        'badQuantity', 
        'totalQuantity'
    ]

    COLUMNS_ORDER = [
        'Workplace',
        'Workplace name', 
        'Manufacturing reference',
        'Manufacturing reference name',
        'Manufacturing order',
        'Order name',
        'Phase', 'Phase name' ,
        'Aggrupation period', 'Shift', 
        'goodQuantity',
        'badQuantity',
        'totalQuantity',
        'instantProductionRatePCH',
        'OEE',
        'performance',
        'availability',
        'quality',
    ]

    SHEET_NAME = SHEET_NAME
    START_ROW = 8
    DEFINED_NAME = 'ReportData'