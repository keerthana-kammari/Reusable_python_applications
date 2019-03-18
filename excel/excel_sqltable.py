import sqlite3
import pyodbc
import pandas as pd
import numpy as np
import xlrd

#Read excel data
data = pd.read_excel('SampleData.xlsx')
#Open the workbook and define the worksheet
book = xlrd.open_workbook('SampleData.xlsx')
sheet = book.sheet_by_name('SalesOrders') #sheet = book.sheet_by_index(0)
#Connecting to SQL server
connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server= servername;"
                      "Database=Test;"
                      "Trusted_Connection=yes;")
#Cursor object is called to send commands to SQL and fetch records
crs = connection.cursor()
#Create the Insert INTO SQL query
query = """INSERT INTO sales_order (OrderDate, Region, Rep, Item, Units, Unit_Cost, Total) VALUES(?, ?, ?, ?, ?, ?, ?)"""

# grab existing row count in the database for validation later
crs.execute("SELECT count(*) FROM sales_order")
before_import = crs.fetchone()

#Create a for loop to iterate through each row in XLS file, starting at row2 to skip the headers
for r in range(1, sheet.nrows):
    OrderDate = sheet.cell(r, 0).value
    Region  = sheet.cell(r, 1).value
    Rep = sheet.cell(r, 2).value
    Item = sheet. cell(r, 3).value
    Units = sheet.cell(r, 4).value
    Unit_Cost = sheet.cell(r, 5).value
    Total = sheet.cell(r, 6).value
    #Assign values from each row
    values = (OrderDate, Region, Rep, Item, Units, Unit_Cost, Total)
    #Execute sql query
    crs.execute(query, values)

#Commit the transaction
connection.commit()

crs.execute("""SELECT COUNT(*) FROM sales_order""")
result = crs.fetchone()

print((result[0] - before_import[0] == len(data.index))) # should return True
connection.close()
print("Successfully imported ", sheet.ncols, "rows and", sheet.nrows, " columns")
