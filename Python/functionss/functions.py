   #!____FUNCTIONS____
#! (1):BUILT IN FUNCTIONS
#! (2):USER DEFINED FUNCTIONS;
#?eg:
# def function_name():
#     print("Helloooo")
# function_name()      

#! METHOD(1):WITHOUT ARG AND NO RETURN TYPE
#? eg:(SUM)
# def add():
#     num1=int(input("Enter a num:"))
#     num2=int(input("Enter a num:"))
#     sum=num1+num2
#     print(sum)
# add()    

#? PROBLEM:FIND PRODUCT OF 3 NUMS
# def prod():
#     num1=int(input("Enter a num:"))
#     num2=int(input("Enter a num:"))
#     num3=int(input("Enter a num:"))
#     product=(num1*num2*num3)
#     print(product)
# prod()    

#! METHOD(2):WITH ARG AND NO RETURN TYPE
#? eg:
# def add(num1,num2):
#     res=num1+num2
#     print(res)
# add(20,50)
#? eg
# n1=int(input("Enter a num:"))
# n2=int(input("Enter a num:"))
# def add(num1,num2):
#     res=num1+num2
#     print(res)
# add(n1,n2)    

#! METHOD(3):WITH ARG AND RETURN TYPE
# def add(n1,n2):
#     sum=n1+n2
#     return sum
# res=add(30,50)
# print("Sum:",res)

# print(res*3)

#?(1) PROBLEM:CREATE A FUNCTION FOR FINDING FACT OF A NUMBER
# n=int(input("Enter a number:"))
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     print(fact)    
# factorial(n)   

#? (2):PROBLEM:PROBLEM:CREATE A FUNCTION FOR FINDING FACT OF A NUMBER(WITH RETURN)
# n=int(input("Enter a number:"))
# def fac(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact
# data=fac(n)
# print(data)

#? PROBLEM:Write a function that reads a number from the user and prints whether it is even or odd.
# num=int(input("Enter num:"))
# def ev_odd():
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")   
# ev_odd()         

#? PROBLEM: Write a function that accepts a string as an argument and prints whether it is a palindrome.
# str=input("Enter the string:")       
# def pali(st):
#     if st==st[::-1]:
#         print("Palindrome")
#     else:
#         print("Not palindrome")    
# pali(str)

#? PROBLEM:Write a function that accepts three numbers and returns the largest among them.
# n1=int(input("enter 1st number:"))
# n2=int(input("enter 2nd number:"))
# n3=int(input("enter 3rd number:"))
# def large(num1,num2,num3):
#     if num1>num2 and num1>num3:
#         largest=num1
#     elif num2>num1 and num2>num3:
#         largest=num2
#     else:
#         largest=num3 
#     return largest     
# res=large(n1,n2,n3)
# print(res)

#? PROBLEM: Write a function that accepts a list of integers and returns the sum of all even numbers.
# lst=[10,20,15,4,3,2,9]
# def ev_sum(listt):
#     total=0
#     for i in listt:
#         if i%2==0:
#             total+=i
#     return total
# even_sum=ev_sum(lst)
# print(even_sum)

#? PROBLEM:Write a function that accepts a list and prints all prime numbers present in it.
# numbers=[10,20,2,4,3,15,19,7]
# def prime_lst(lst):
#    for num in lst:
#         if num>1:
#             for i in range(2,num):
#                 if num%i==0:
#                     break
#             else:
#                print(num)
# prime_lst(numbers)






 





                             
                

          








      



    

    
   






