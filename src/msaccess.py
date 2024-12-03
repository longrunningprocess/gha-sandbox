import pyodbc

access_jet_drivers = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]

print("JET drivers found: " + access_jet_drivers)
