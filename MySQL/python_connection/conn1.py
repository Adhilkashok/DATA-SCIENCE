 #! __PYTHON MySQL CONNECTION__
#? => ALLOWS A PYTHON PROGRAM TO COMMUNICATE WITH A MYSQL DATABASE

#! PACKAGE --> mysql-connector-python

#? pip command
#?pip install mysql-connector-python

import mysql.connector

#? Connection object
# syntax:myconn=mysql.connector.connect(host='server location',
#                               user='root',
#                               password='mysql password')

myconn=mysql.connector.connect(host='localhost',
                               user='root',
                               password='adhisqlroot')
# print("connection successfull")

#? Cursor object-> An object used to send SQL commands from Python to MySQL.
cursor=myconn.cursor()

#? Listing Databases
cursor.execute("SHOW DATABASES")

#? Fetching and displaying each databases
for db in cursor:
    print(db)

#? Close connection
myconn.close()



