#!/usr/bin/python

## open the database 
import sqlite3 
conn = sqlite3.connect('GN_test.db')
print('Opened database successfully')

## INSERT Operation 
## This operation is used to create records in the database table in 'GN_test.db'


#person01  
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES(10, 'Felix', 27, 'Dar es salaam', 50000.00)"); 

#person02  
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES(11, 'Mary', 24, 'Arusha', 55000.00)"); 

#person03  
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES(12, 'Lucas', 30, 'Nairobi', 60000.00)"); 

#person04  
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES(13, 'Colman', 25, 'Kilifi', 50000.00)"); 

#person05  
conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES(14, 'Anna', 27, 'Mbeya', 70000.00)"); 

conn.commit() # saves the changes made

print('Records created successfully')

conn.close()