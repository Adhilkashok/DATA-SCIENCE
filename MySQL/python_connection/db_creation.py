import mysql.connector

#? connection object
myconn=mysql.connector.connect(host='localhost',
                               user='root',
                               password='adhisqlroot')

#? cursor object
cursor=myconn.cursor()

#? query execution
cursor.execute("create database std_june")
print("Database created")
