import pyodbc

for driver in [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]:
	print(driver)
