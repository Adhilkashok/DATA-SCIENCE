import mysql.connector
myconn=mysql.connector.connect(host='localhost',
                               user='root',
                               password='adhisqlroot',
                               database='std_june')
cursor=myconn.cursor()
# query="""create table employee(emp_id int primary key, emp_name varchar(50), dept varchar(50),salary int)"""
# cursor.execute(query)
#? inserting values
# query1="""insert into employee values(100,"Rahul","HR",50000),
#                                      (101,"Arjun","IT",40000),
#                                      (102,"Anu","IT",35000)"""
# cursor.execute(query1)

#? COMMIT() -> permanently saves the changes to the database - insert,update,delete
myconn.commit()

# print("Table created")

# Fetching data
# cursor.execute("Select * from employee")

#? fetchall():Returns all records
# for rows in cursor.fetchall():
#     print(rows)


#? fetchone():Returns only one record 
# row=cursor.fetchone()   
# print(row)

#? fetchmany(n):Returns specified n no.of rows
# row=cursor.fetchmany(2)
# print(row)

cursor.execute("Select dept from employee")
for rows in cursor.fetchall():
    print(rows)