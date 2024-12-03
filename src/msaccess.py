import pyodbc

# https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-Microsoft-Access
access_jet_drivers = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]
print("JET drivers found: " + ", ".join(access_jet_drivers))
