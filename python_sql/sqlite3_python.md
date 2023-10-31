## ACCESSING SQL DATABASE USING SQLITE3 MODULE IN PYTHON 
### The following presents basic description of how to access any SQL (Sequel) database using a database management module in python, called sqlite3 
### For more information about sqlite3, visit the following site: `https://www.tutorialspoint.com/sqlite/index.htm`

### 01 Connect to the existing database or crate a new one 
#### The first step is to connect the python api to the an existing database or create one using sqlite3. Python contains this module by default. 
#### So, the first step is to import the module, then connect to a database
```python
## Accessing an SQL Database with python using sqlite3 

## import sqlite3 module 
import sqlite3 

## connect to an existing database or create one (in this case we will create a database) 
conn = sqlite3.connect('GN_test.db')

print('Opened database successfully')

```
#### Output; 
`Opened database successfully`

#### The corresponding python script is found in `open_db.py`

### 02 Create a table in the newly created database; `GN_test.db`
#### In this step, a table is created containing necessary information such as primary key, type of values for each category, as well as key constraints to ensure valid and correct data is put in the database
```python
## open the database 
import sqlite3 
conn = sqlite3.connect('GN_test.db')
print('Opened database successfully')

## Create a table in 'GN_test.db' database
conn.execute(''' CREATE TABLE COMPANY 
          (ID INT PRIMARY KEY  NOT NULL, 
          NAME  TEXT NOT NULL, 
          AGE INT NOT NULL, 
          ADDRESS CHAR(50), 
          SALARY REAL);''')

print('Table created successfully!')

conn.close() # closes the db connection 
```
#### Output; 
```markdown
Opened database successfully
Table created successfully!
```
#### The corresponding python script is found in `Create_table.py`

### 03 Insert records in the newly created table 
#### A set of values corresponding to the categories created in the table will then be put in the table using `INSERT` Operator 
```python
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
```
#### Output;
```markdown
Opened database successfully
Records created successfully
```
#### The corresponding python script is found in `INSERT_Op.py`

### 03 Fetch and display records in COMPANY table using `SELECT` Operator 

```python
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
```
#### Output; 
```markdown
Opened database successfully
ID = 10
NAME = Felix
ADDRESS = Dar es salaam
SALARY = 50000.0
ID = 11
NAME = Mary
ADDRESS = Arusha
SALARY = 55000.0
ID = 12
NAME = Lucas
ADDRESS = Nairobi
SALARY = 60000.0
ID = 13
NAME = Colman
ADDRESS = Kilifi
SALARY = 50000.0
ID = 14
NAME = Anna
ADDRESS = Mbeya
SALARY = 70000.0
Operation done successfully
```
#### The corresponding python script is found in `SELECT_Op.py`

### 04 Update records in the COMPANY table using `UPDATE` Operator 
#### In this step, salary information belonging to individual with id no 14 was updated to 80000.00
```python
## open the database 
import sqlite3 
conn = sqlite3.connect('GN_test.db')
print('Opened database successfully')

## UPDATE Operation 
## Update information in 'GN_test.db'


conn.execute("UPDATE COMPANY set SALARY = 80000.00 where ID = 14")
conn.commit()
print('Total number of rows updated:', conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

for row in cursor: 
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3])
print('Operation done successfully')
conn.close()
```
#### Output;
```markdown
Opened database successfully
Total number of rows updated: 1
ID = 10
NAME = Felix
ADDRESS = Dar es salaam
SALARY = 50000.0
ID = 11
NAME = Mary
ADDRESS = Arusha
SALARY = 55000.0
ID = 12
NAME = Lucas
ADDRESS = Nairobi
SALARY = 60000.0
ID = 13
NAME = Colman
ADDRESS = Kilifi
SALARY = 50000.0
ID = 14
NAME = Anna
ADDRESS = Mbeya
SALARY = 80000.0
Operation done successfully
```
#### The corresponding python script is found in `UPDATE_Op.py`

### 04 Delete records from the COMPANY table using `DELETE` Operator 
#### In this step, information in the table corresponding to id no 11, was removed 
```python
## open the database 
import sqlite3 
conn = sqlite3.connect('GN_test.db')
print('Opened database successfully')

## DELETE Operation 
## Do away with some of the information and display the remaining data 

conn.execute("DELETE FROM COMPANY where ID = 11")
conn.commit()
print("Total number of rows deleted:", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")

for row in cursor: 
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3])
print('Operation done successfully')
conn.close()
```
#### Output;
```markdown
Opened database successfully
Total number of rows deleted: 1
ID = 10
NAME = Felix
ADDRESS = Dar es salaam
SALARY = 50000.0
ID = 12
NAME = Lucas
ADDRESS = Nairobi
SALARY = 60000.0
ID = 13
NAME = Colman
ADDRESS = Kilifi
SALARY = 50000.0
ID = 14
NAME = Anna
ADDRESS = Mbeya
SALARY = 80000.0
Operation done successfully
```
#### The corresponding python script is found in `DELETE_Op.py`






