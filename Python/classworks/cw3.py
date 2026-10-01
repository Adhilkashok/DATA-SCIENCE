 #* Create a Python program using Object-Oriented Programming (OOP) that includes a class called Employee with attributes such as id, name, age, designation, experience (in years), and salary. The class should include methods to display employee details and update the designation.
#* It should also include a method to check promotion eligibility where an employee is eligible for promotion if experience is 5 years or more and age is above 30; otherwise, the employee is not eligible.
#* Create at least one object of the Employee class, assign values directly, and display all the details along with the promotion eligibility result.
# class Employee:
#     def emp_details(self):
#         print("ID:",self.id)
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Designation:",self.designation)
#         print("Experience:",self.experience,"Years")
#         print("Salary:",self.salary)
#     def update_designation(self,new_designation):
#         self.designation=new_designation
#     def check_promotion(self):
#         if self.experience>=5 and self.age>30:
#             print("Eligible for Promotion")
#         else:
#             print("Not Eligible for Promotion")
# emp1=Employee()
# print("Before:")
# emp1.id=81
# emp1.name="Adhil"
# emp1.age=31
# emp1.designation=" Junior Data scientist"
# emp1.experience=4
# emp1.salary=50000
# emp1.emp_details()
# emp1.update_designation("Senior Data scientist")
# emp1.check_promotion()
# print("\nAfter Updating Designation:")
# emp1.emp_details()

#* Define a function that takes a string as an argument and returns a dictionary where the keys are the characters of the string and the values are the number of occurrences of each character.
#* Ignore spaces while counting the characters.
#* Example:
#* Input:s = "hello world"
#* Output:
#* {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
# S=input("Enter a string:")
# def str_count(s):
#     d={}
#     for st in s:
#         if st==" ":
#             continue
#         if st in d:
#             d[st]+=1
#         else:
#             d[st]=1
#     return d
# print(str_count(S))
                
