 #?! _DECISION MAKING STATEMENTS_
#! (1):IF STATEMENTS
# num=10
# if num>0:
    # print(" Yes it is greater")

#?PROBLEM:take a num from user and check whether it is greater than 100
# num=int(input("Enter a number:"))    
# if num>100:
#     print("Yes it is greater")

#?PROBLEM:take a num from user and check whether it is 50 or not
# num=int(input("enter a num:"))
# if num==50:
    # print("yes it is")

#?PROBLEM:take a num from user and check it is Even
# num=int(input("enter a num:"))
# if num%2==0:
    # print("yes it is even")


#! (2):IF-ELSE STATEMENTS
#?PROBLEM:take a num from user and check it is Even or not
# num=int(input("enter a num:"))
# if num%2==0:
    # print("even")
# else:
    # print("not even")    

#? PROBLEM:CHECK WHETHER A NUM IS POSITIVE OR NOT
# num=int(input("Enter a number:"))
# if num>0:
    # print("positive")
# else:
    # print("not positive")    

#? PROBLEM:CHECK WHETHER A PERSON IS ELIGIBLE FOR VOTING
# age=int(input("enter the age:"))
# if age>=18:
    # print("eligible")
# else:
    # print("not eligible")    

#? PROBLEM:TAKE 2 NUMS FROM USER AND FIND THE GREATEST AMONG TWO
# num1=int(input("Enter a number"))
# num2=int(input("Enter another number"))
# if num1>num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater")

#? 12-CHECK WHETHER A NUM/WORD  IS PALINDROME
# num=input("Enter the number:")
# if num==num[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")    


#! (3):IF...ELIF...ELSE STATEMENTS
# num1=20
# num2=2
# if num1>num2:
#     print("num1 is greater")
# elif num2>num1:
#     print("num2 is greater")
# else:
#     print("they are equal")   

#? PROBLEM:CHECK IF A NUM IS POSITIVE NEGATIVE OR ZERO  
# num=int(input("Enter a number:"))
# if num>0:
#     print("num is positive")
# elif num<0:
#     print("num is negative")
# else:
#     print("num is zero")    


#? PROBLEM:TAKE 5 MARKS OUT OF 20 AND FIND TOTAL THEN PRINT THE GRADE USING IF-ELIF-ELSE.
# m1=int(input("Enter maths mark:"))
# m2=int(input("Enter physics mark:"))
# m3=int(input("Enter hindi mark:"))
# m4=int(input("Enter english mark:"))
# m5=int(input("Enter science mark:"))
# total=m1+m2+m3+m4+m5
# if total>=90:
#     print("Grade is A")
# elif total>=75:
#     print("Grade is B")
# elif total>=50:
#     print("Grade is C")    
# else:
#     print("Fail")        

#? PROBLEM:TAKE A CHARACTER FROM THE USER AND CHECK WHETHER IT IS A VOWEL OR CONSONANT
# ch=input("Enter the character:")
# if ch in "aeiouAEIOU":
#      print("Vowel")
# else:
#      print("Consonant")

#? PROBLEM:ACCEPT THE NO OF UNITS CONSUMED AND CALCULATE THE ELECTRIC BILL
#? FIRST 100 UNITS -5 PER UNIT
#? LESS THAN 2OO UNITS-7 PER
#? ABOVE 200 UNITS-10 PER UNIT
#? DISPLAY THE TOTAL BILL AMOUNT   
# units=int(input("Enter the no of units:"))
# if units<=100:
#     bill=units*5
# elif units<=200:
#     bill=100*5+((units-100)*7)
# else:
#     bill=100*5+100*7+((units-200)*10)
# print("Your current bill amount is",bill) 

#? PROBLEM:ACCEPT THE PURCHASE AMOUNT AND MEMBERSHIP STATUS(YES/NO)
#? IF PURCHASE AMOUNT IS ABOVE 5000
#? MEMBER -20% DISCOUNT
#? NON MEMBER-10% DISCOUNT
#? OTHERWISE:
#? MEMBER-5% DISCOUNT
#? NON MEMBER-NO DISCOUNT
#? DISPLAY THE FINAL AMOUNT
# amount=int(input("Enter the amount:"))
# ms=input("Membership status (yes/no):").lower()
# if amount>=5000:
#     if ms=="yes":
#         discount=amount*20/100
#         final_amount=amount-discount
#         print("final amount is",final_amount)
#     else:
#         discount=amount*10/100
#         final_amount=amount-discount
#         print("final amount is",final_amount)
# elif amount<5000:
#     if ms=="yes":
#         discount=amount*5/100
#         final_amount=amount-discount
#         print("final amount is",final_amount)
#     else:
#         print("No discount, Pay the amount",amount) 
# else:
#     "invalid"        


#? PROBLEM:Write a Python program to accept the following details of a student:
# Name
# Age
# Attendance percentage
# Marks in Mathematics
# Marks in Science
# Determine the scholarship eligibility using these rules:
# 1. If the student's attendance is 75% or more:
# If both Mathematics and Science marks are 80 or above:
# If the age is 18 or below, print:
# Eligible for Full Scholarship
# Otherwise, print:
# Eligible for Partial Scholarship
# Otherwise, print:
# Not Eligible: Marks are too low
# 2. If the attendance is below 75%, print:
# Not Eligible: Attendance is insufficient

# name=input("Enter the name of the student:")
# age=int(input("Enter the age:"))
# attendance=float(input("Enter the percentage:"))
# maths=int(input("Maths Mark:"))
# science=int(input("Science Mark:"))
# if attendance>=75:
#     if maths>=80 and science>=80:
#         if age<=18:
#             print("Eligible for  full scholorship")
#         else:
#             print("Eligible for partial scholorship")
#     else:
#         print("Not eligible: Marks are too low")  
# else:
#     print("Not eligible:Attendance is insufficient")     


#? PROBLEM:Write a Python program to accept a person's name, age, ticket type (Regular/Premium), and guardian availability (Yes/No).
# If age is 18 or above:
# If ticket type is Premium:
# If the person has a valid ID, print "Premium Entry Allowed".
# Otherwise, print "Premium Entry Denied".
# Otherwise, print "Regular Entry Allowed".
# If age is below 18:
# If a guardian is available, print "Entry Allowed with Guardian".
# Otherwise, print "Entry Denied".  
      
# name=input("Enter the name:")
# age=int(input("Enter the age:"))
# ticket=input("Enter the ticket type(regular/premium):").lower()
# id=input("Have a valid ID(yes/no):").lower()
# guardian=input("Guardian availability(yes/no):").lower()
# if age>=18:
#     if ticket=="premium":
#         if id=="Yes":
#             print("Premium Entry Allowed")
#         else:
#             print("Premium Entry Denied")
#     else:
#         print("Regular Entry Allowed")    
# else:
#     if guardian=="Yes":
#         print("Entry Allowed With Guardian")
#     else:
#         print("Entry Denied")                   


#? 15-FIND SECOND LARGEST NUMBER FROM 3 NUMBERS
# num1=int(input("Enter the 1st num:")) 
# num2=int(input("Enter the 2nd num:")) 
# num3=int(input("Enter the 3rd num:")) 
# if num1>num2 and num1>num3:
#     if num2>num3:
#         print("The 2nd largest num is:",num2)
#     else:
#         print("The second largest num is:",num3)
# elif num2>num1 and num2>num3:
#     if num1>num3:
#         print("The 2nd largest num is:",num1)            
#     else:
#         print("The 2nd largest num is:",num3)
# else:
#     if num1>num2:
#         print("The 2nd largest num is:",num1)
#     else:
#         print("The 2nd largest num is:",num2) 
            




