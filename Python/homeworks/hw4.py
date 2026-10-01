 #? (1)PROBLEM:Write a program to print all even numbers between 1 and 20.
# i=2
# while i<=20:
#     print(i)
#     i=i+2

#? (2)PROBLEM:Write a program to print all odd numbers between 1 and 20.
# i=1
# while i<20:
#     print(i)
#     i=i+2

#? (3)PROBLEM:Print numbers from 1 to 50, but stop when you find the first multiple of 7 greater than 20.
# i=1
# while i<=50:
#     if i%7==0 and i>20:
#         break
#     print(i)
#     i+=1

#? (4)PROBLEM:Print numbers from 1 to 30, but skip numbers that are divisible by both 2 and 3.
# i=1
# while i<=30:
#     if i%2==0 and i%3==0:
#         i+=1
#         continue
#     print(i)
#     i+=1

#? (5)PROBLEM:Print numbers from 1 to 10. When the number is 5, use pass and continue printing the remaining numbers.
# i=1
# while i<=10:
#     if i==5:
#         pass
#     print(i)
#     i+=1

#? (6)PROGRAM:PRINT ALL LETTERS OF A WORD EXCEPT THE VOWELS
# word=input("Enter the word:")
# i=0
# while i<len(word):
#     if word[i] in "aeiouAEIOU":
#         i+=1
#         continue
#     print(word[i],end="")
#     i+=1

#? (7)PROGRAM:Use pass inside a loop that checks whether a number is positive or negative.
# i=1
# while i<=5:
#     num=int(input("Enter a number:"))
#     if num>0:
#         pass
#         print("Positive")
#     else:
#         print("Negative")
#         i+=1

#? (8)PROGRAM:Find the sum of the first N natural numbers using a for loop.
# n=int(input("Enter the value of N:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print("Sum is:",sum)

#? (9):Find the factorial of a number using a for loop.
# num=int(input("Enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("Factorial is:",fact)    

#? (10):Print squares of numbers from 1 to 10
# for i in range(1,11):
#     sq=i*i
#     print("square of",i,"=",sq)    

#? (11):Count how many even numbers are between 1 and 100.
# count=0
# for i in range(1,101,2):
#         count=count+1
# print("Total even numbers are:",count) 

#? (12): Count how many odd nums are btw 1 and 100.
# count=0
# for i in range(1,101):
#     if i%2!=0:
#         count=count+1
# print("Total odd numbers are:",count)       

#? (13):Print the last 20 natural numbers before 100.
# for i in range(80,100):
#     print(i)

#? (14):Print all numbers between 1 and N that are divisible by 3 but not by 5.
# n=int(input("Enter nth number:"))
# for i in range(1,n+1):
#     if i%3==0 and i%5!=0:
#         print(i)

#? (15):FIND ALL FACTORS OF A GIVEN NUMBER
# num=int(input("Enter the number:"))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i, end=" ")

#? (16):PRINT ALL PERFECT NUMS BTW 1-1000
# for num in range(1,1001): 
#     total=0
#     for j in range(1,num):
#         if num%j==0:
#             total=total+j
#     if total==num:
#         print(num) 

#? (17):PRINT ALL PAIRS OF NUMS BTW 1 AND 10 WHOSE SUM IS 10
# for i in range(1,11):
#     for j in range(1,11):
#         if i + j== 10:
#             print(i,j)

#? (18):INVERTED RIGHT TRIANGLE
# for i in range(5,0,-1):
#     for j in range(1,1+i):
#         print("*",end=" ")   
#     print()    

#? (19):HOLLOW SQUARE(5X5)  
# for i in range(5):
#     for j in range(5):
#         if i==0 or i==4 or j==0 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")  
#     print()          

  

