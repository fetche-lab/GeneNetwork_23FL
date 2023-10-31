#!/usr/bin/python 

## open the database 
import sqlite3 
conn = sqlite3.connect('GN_test.db')
print('Opened database successfully')

## Create a table in 'GN_test.db' databasE
conn.execute(''' CREATE TABLE COMPANY 
          (ID INT PRIMARY KEY  NOT NULL, 
          NAME  TEXT NOT NULL, 
          AGE INT NOT NULL, 
          ADDRESS CHAR(50), 
          SALARY REAL);''')

print('Table created successfully!')

conn.close() # closes the db connection 