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