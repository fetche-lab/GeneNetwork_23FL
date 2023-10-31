#!/usr/bin/python 

## Accessing an SQL Database with python using sqlite3 

## import sqlite3 module 
import sqlite3 

## connect to an existing database or create one 
## in this case we will create a database 
conn = sqlite3.connect('GN_test.db')
print('Opened database successfully')