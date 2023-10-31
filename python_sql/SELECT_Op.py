#!/usr/bin/python

## open the database 
import sqlite3 
conn = sqlite3.connect('GN_test.db')
print('Opened database successfully')

## SELECT Operation 
## Fetches and displays information found in 'GN_test.db'
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

for row in cursor: 
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3])
print('Operation done successfully')
conn.close()