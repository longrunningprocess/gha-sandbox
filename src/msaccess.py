import pyodbc

# https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-Microsoft-Access
access_drivers = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]
print(access_drivers)

# conn_str = (
#     r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
#     r'DBQ=D:\a\gha-sandbox\gha-sandbox\src\empty.mdb;'
#     )
# cnxn = pyodbc.connect(conn_str)
# crsr = cnxn.cursor()
# for table_info in crsr.tables(tableType='TABLE'):
#     print(table_info.table_name)
