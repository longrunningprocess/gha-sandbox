import pyodbc

access_drivers = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]

print(access_drivers)
