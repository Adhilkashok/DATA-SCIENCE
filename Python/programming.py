 #! (1):PROCEDURAL PROGRAMMING(PP):Is organized as a sequence of functions that operate on data.
 #! (2):OBJECT ORIENTED PROGRAMMING(OOPS):Is organized around Objects and Classes.
#? Creating a class
#?  eg:     (use caps for 1st letter)
# class Student:
    # pass

#? Object creation
#? eg:
# class Student:
#     pass
# s1=Student()
# print(s1)


# Adding attributes manually
#? eg:
# class Student:
#     pass
# s1=Student()
# s2=Student()
# s1.name="Adhil"
# s2.name="Rahul"
# s1.age=21
# s2.age=22
# print("Name=",s1.name)
# print("Age=",s1.age)
# print("Name=",s2.name)
# print("Age=",s2.age)

#? eg:
# class Mobile:
#     pass
# m1=Mobile()
# m1.brand="Redmi"
# m1.storage="256GB"
# print(m1.brand)
# print(m1.storage)

#? create a class book
#? create 1 object and store book name,author,price
# class Book:
#     pass
# b1=Book()
# b1.name="Harry Potter"
# b1.author="j.K.Rowling"
# b1.price=510
# print(b1.name)
# print(b1.author)
# print(b1.price)

#? create a class employeeeeeeeee
#? create one object and store empname,dept,salary
# class Employee:
#     pass
# e1=Employee()
# e1.empname="Adhil"
# e1.dept="Data Science"
# e1.salary=30000
# print(e1.empname)
# print(e1.dept)
# print(e1.salary)


#? METHODS
#? eg:
# class Student:
#     def display(self):
#         print("Welcome to class")
# s1=Student()
# s1.display()        

# class Student:
#     def display(self):
#         print("Name:" "Adhil")
# s1=Student()
# s1.display()        


#? CONSTRUCTOR/MAGIC METHOD
#? syntax:
# class Student:
#     def __init__(self):
#         print("object created")
# s1=Student()    
#     
#? eg:
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Adhil",21)    
# s2=Student("Rahul",22)
# print(s1.name,s1.age)
# print(s2.name,s2.age)    
        

#? METHOD USING OBJECT DATA
#? eg:
# class Student:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print("student name is",self.name)
# s1=Student("Adhil")
# s1.display()        
        
#? eg
# class Student:
#     cname="Data Science"
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print("student name is",self.name)    
# s1=Student("Adhil") 
# s1.display()
# print(s1.cname)       
            

#? eg
# class Car:
#     def __init__(self,brand,colour):
#         self.brand=brand
#         self.colour=colour
#     def start(self):
#         print(self.colour,self.brand, "is started") 
#     def move(self):
#         print(self.colour,self.brand,"is moving")
#     def stop(self):
#         print(self.colour,self.brand,"is stopped")
# c1=Car("BMW","Black")
# c1.start()
# c1.move(),
# c1.stop()
        


#* Task (1): Mobile Class**
#* Create a class named Mobile.

#* Attributes:
#* Brand
#* Model

#* Methods:
#* call()
#* message()

#* Sample Output:
#* Samsung is making a call.
#* Samsung sent a message.

# class Mobile:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def call(self):
#         print(self.brand,self.model,"is making a call ")    
#     def message(self):
#         print(self.brand,self.model,"sent a message")
# m1=Mobile("samsung","S26")
# m1.call()
# m1.message()            

#* Task (2): Bank Account** 
#* Create a class named BankAccount.
#* Attributes:
#* Account Holder Name
#* Balance

#* Methods:
#* check balance
#* deposit(amount)
#* withdraw(amount)

#* Sample Output:
#* Deposited: 5000
#* Current Balance: 15000
#* Withdrawn: 3000
#* Current Balance: 12000
#* Hint: Update the balance inside the methods.        
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def check_balance(self):
#         print("Current balance:",self.balance)
#     def deposit(self,amount):
#         self.balance+=amount   
#         print("Deposited:",amount)
#         print("current balance:",self.balance)
#     def withdraw(self,amount):
#         if amount>=self.balance:
#             print("Insufficient balance")
#         else:    
#          self.balance-=amount
#          print("withdrawn:",amount)
#          print("Current balance:",self.balance)    
# acc=BankAccount("Adhil",15000)        
# acc.check_balance()
# acc.deposit(5000)
# acc.withdraw(1000)



#* Task (3): Shopping Cart
#* Create a Product class with:
#* Attributes: product_id, product_name, price, quantity
#* Methods:
#* Calculate the total cost.
#* Apply a 10% discount if the total cost exceeds ₹5000.
#* Display the final bill.
# class Product:
#     def __init__(self,id,name,price,quantity):
#         self.id=id
#         self.name=name
#         self.price=price
#         self.quantity=quantity
#     def total_cost(self):
#         self.total=self.price*self.quantity
#     def discount(self):
#         if self.total>5000:
#             dis=(self.total*10)/100
#             bill=self.total-dis
#             print("Total bill:",bill)
#         else:
#             print("Total bill:",self.total)    
# pr=Product(101,"Protein Powder",1000,6)   
# pr.total_cost()
# pr.discount()         



#* Task (4): Student Management
#* Create a Student class with the following:
#* Attributes: student_id, name, course, marks
#* Methods:
#* Display student details.
#* Check whether the student has passed (pass mark = 40).
# class Student:
#     def __init__(self,id,name,course,marks):
#         self.id=id
#         self.name=name
#         self.course=course
#         self.marks=marks
#     def Std_details(self):
#         print("Student_ID:",self.id)
#         print("Student_Name:",self.name)
#         print("Course:",self.course)
#         print("Marks:",self.marks)
#     def result(self):
#         if self.marks>=40:
#             print("Student has passed")
#         else:
#             print("Student has failed")
# s1=Student(100,"Adhil","Bsc Maths",39)
# s1.Std_details()
# s1.result()                   
                     


#* Task(5):Student Management using Inheritance
#* Create a Student class with the following attributes:
#* student_id
#* name
#* course
#* Create another class Marks that inherits from the Student class.
#* The Marks class should have:
#* marks as an additional attribute.
#* display_details() method to display the student ID, name, course, and marks.
#* check_result() method to check whether the student has passed or failed.
#* The pass mark is 40.
#* Create an object of the Marks class and display the student's details and result. 

# class Student:
#     def __init__(self, student_id, name, course):
#         self.student_id = student_id
#         self.name = name
#         self.course = course

# class Marks(Student):
#     def __init__(self, student_id, name, course, marks):
#         self.student_id = student_id
#         self.name = name
#         self.course = course
#         self.marks = marks   

#     def display_details(self):
#         print("Student ID:", self.student_id)
#         print("Name:", self.name)
#         print("Course:", self.course)
#         print("marks:",self.marks)

#     def check_result(self):
#         if self.marks >= 40:
#             print("Result: Passed")
#         else:
#             print("Result: Failed")

# s1 = Marks(101, "Adhil", "Data Science", 30)
# s1.display_details()
# s1.check_result()




#! OOPs-4 PILLERS
#! 1)INHERITENCE:Allows one classs to inherit the properties and methods of another class
#? eg:inherit parent to child.parent features use in child
# class Animal:       #parent class
#     pass
# class dog(Animal):  #child class
#     pass

#? eg:
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     pass
# d1=Dog()
# d1.eat()

#? TYPES OF INHERITENCE
#? (1):SINGLE INHERITENCE=>ONE PARENT CLASS AND ONE CHILD CLASS
#* above programs are examples of this
#? (2):MULTIPLE INHERITENCE=>2 PARENT AND ONE CHILD CLASS
#* eg:
# class Father:
#     def money(self):
#         print("Father's money")
# class Mother:
#     def care(self):
#         print("Mother's care")
# class Child(Father,Mother):
#     pass
# c1=Child()
# c1.money()
# c1.care()

                        

#? (3):MULTILEVEL INHERITENCE:BASE LEVEL,INTERMEDIATE LEVEL,DERIVED LEVEL
#* eg:
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class dog(Animal):
#     pass
# class Puppy(dog):
#     pass
# p1=Puppy()
# p1.eat()        

#? (4):HIERARCHICAL INHERITENCE=>ONE PARENT AND MANY CHILD CLASSES


#! 2)POLYMORPHISM:One Method Can Have Many Forms.(OVERRIDING METHOD)
#* eg:
# class Animal:
#     def eat(self):
#         print("Animal is eating")
# class Dog(Animal):
#     def eat(self):                  # This overrides the parent's eat() method
#       print("dog is barking")
# d1=Dog()
# d1.eat()
 

#! 3)ENCAPSULATION:Keeps the data safe and allow access only through methods.
#* example:
# Think about an ATM.
# U can deposit,withdraw,check money but u cannot directly change your bank balance by opening the ATM

#! 4)ABSTRACTION:Hide unneccessary details and show only essential features.
#* example:
# Car.
# You drive using
# Steering
# Brake
# Accelerator
# You don't need to know how the engine works.            
        



    




                