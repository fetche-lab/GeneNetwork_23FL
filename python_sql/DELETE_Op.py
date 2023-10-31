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