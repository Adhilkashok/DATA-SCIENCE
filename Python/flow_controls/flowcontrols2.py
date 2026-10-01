 #!   _LOOPING STATEMENTS_
#! (1):WHILE LOOP
#? PROBLEM:PRINT 1 TO 10
# i=1
# while i<=10:
#     print(i)
#     i=i+1

#? PROBLEM:PRINT 0 TO 100
# i=0
# while i<=100:
#     print(i)
#     i+=1

#? PROBLEM:PRINT 10 TO 1
# i=10
# while i>=1:
#     print(i)
#     i=i-1

#! (2):FOR LOOP
#? eg:
# lst=[1,3,5,7,89,8]
# for i in lst:
#     print(i)
#? eg:
# for i in "apple":
#     print(i)
#? eg:(BREAK)
# lst=["s","a","l","i","n","i"]
# for i in lst:
#     if i=="i":
#         break
#     print(i)
#? eg:(CONTINUE)
# lst=["a","b","c","d"]
# for i in lst:
#   if i=="c":
#     continue
#   print(i)

#? 1-PROBLLEM:CREATE A TUPLE OF 6 NUMBERS. USE FOR LOOP TO PRINT ALL ELEMENTS OF THE TUPLE
#? 2-PRINT ONLY EVEN NUMBERS ON THAT TUPLE.
# tup=(1,2,3,4,5,6)
# for i in tup:
    # print(i)
# tup=(1,2,3,4,5,6)
# for i in tup:
#     if i%2==0:
#         print(i)    

#? PROBLEM:ACCEPT A SENTENCE FROM THE USER PRINT ALL CHARACTRS EXCEPT SPACES
# ch=input("Enter the character:")
# for i in ch:
#     if i==" ":
#         continue
#     print(i)

#? PROBLEM:ACCEPT A WORD FROM USER.
#? PRINT EACH CHAR ONE BY ONE ,BUT STOP WHEN CHAR IS "a".
# word=input("Enter a word:")
# for i in word:
#     if i=="a":
#         break
#     print(i)

#? PROBLEM:PRINT HELLO WORLD 5 TIMES
# lst=[1,2,3,4,5]
# for i in lst:
#     print("HELLO WORLD")   


#! _RANGE_
#? eg:(PRINT 1 TO 10)
# for i in range(1,11):
#     print(i)
#? eg:(PRINT 1 TO 10 WITH DIFF 2) 
# for i in range(1,11,2):
#     print(i)

#?1 1-PROBLEM:PRINT FROM 10 TO 50
# for i in range(10,51):
#     print(i)

#? 2-PROBLEM:PRINT 20 TO 100 AS[20,25,30,35,....95,100] 
# for i in range(20,101,5):
#     print(i)    

#? 3-PROBLEM:PRINT "HELLO" 10 TIMES
# for i in range(10):
    # print("Hello")

#? 4-PROBLEM:PRINT FROM 15 TO 5 - (REVERSE)
# for i in range(15,4,-1):
#     print(i)

#? 5-PROBLEM:PRINT ALL EVEN FROM 2-20
# for i in range(2,21):
#     if i%2==0:
#      print(i)
#? 6-PROBLEM:PRINT ALL ODD FROM 36-90
# for i in range(36,91):
#     if i%2!=0:
#      print(i)
#? 7-PROBLEM:PRINT MULTIPLICATION TABLE FOR A NUMBER TAKEN FROM USER
# num=int(input("Enter a number:"))
# a=int(input("Enter the start:"))
# b=int(input("Enter the end:"))
# for i in range(a,b+1):
#         print(f"{i}x{num}={num*i}")

#? 8-PROBLEM:PRINT CUBES OF NUMBERS FROM 1-20
# for i in range(1,21):
#     cubes=i**3
#     print(cubes)

#? 8-PROBLEM:PRINT ALL PRIME NUMS BTW 1-100
# for num in range(2,101):
#     Prime=True
#     for i in range(2,num):
#         if num%i==0:
#             Prime=False
#             break
#     if Prime:
#         print(num,end=" ")

#? 9-PROBLEM:GENERATE FIBINOCCI SERIES UPTO A NUMBER N TERMS.
# num=int(input("Enter Nth number:"))
# a=0
# b=1
# for i in range(num):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

#? 10:COUNT HOW MANY EVEN AND ODD NUMBERS BTW 1-100
# even=0
# odd=0
# for i in range(1,101):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("Even count:",even) 
# print("Odd count:",odd)           


#? 11:CHECK WHETHER A STRING IS PALINDROME OR NOT using if-else
# st=input("Enter a string:")  
# print(st[::-1])
# if st==st[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")    


#? 12:CREATE SIMPLE ATM MENU USING WHILE LOOP; (1)CHECK BALANCE, (2)DEPOSIT, (3)WITHDRAW, (4)EXIT
# balance=500000
# while True:
#     print("\n----ATM----")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Exit")

#     choice=int(input("Enter choice:"))
#     if choice==1:
#         pin=int(input("Enter your PIN:"))
#         print(f"Current balance is {balance}")
#     elif choice==2:
#         amount=int(input("Enter deposit amount:"))   
#         pin=int(input("Enter your PIN:"))
#         balance=balance+amount
#         print("Amount deposited successfully")
#         print("New balance:",balance)
#     elif choice==3:
#         amount=int(input("Enter withdrawal amount:"))
#         pin=int(input("Enter your PIN:"))
#         if amount<=balance:
#             balance=balance-amount
#             print("Please collect your cash")    
#             print("Remaining balance:",balance)
#         else:
#             print("Insufficient balance")
#     elif choice==4:
#         print("Thank you for visiting the ATM")    
#         break
#     else:
#         print("Invalid choice! Please try again")    



#! NESTED FOR LOOP    
#? eg(1):
# adj=["red","big"]
# fruits=["apple","cherry"]
# for i in adj:
#     for j in fruits:
#         print(i,j)

#? eg(2):
# for i in range(3):
#     for j in range(2):
#         print(i,j)

#? eg(3):
# for i in range(1,6):
#     print(i,end=" ")

#? eg(4):
# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print()        

#? eg(5):
# for i in range(3):
#     for j in range(3):
#         print(j,end=" ")
#     print()    

#? eg(6):(RIGHT TRIANGLE)
# for i in range(1,5):
#     for j in range(1,1+i):
#         print("*",end=" ")
#     print()

#? eg:(Decreasing stars)
# for i in range(4, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

#? eg:(Right Aligned Stars()
# for i in range(1, 5):
#     for j in range(4 - i):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     print()

#? eg:(7)            
# for i in range(1,5):
#     for j in range(1,1+i):
#         print(j,end=" ")
#     print()    

#? eg:(8)
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()    

# ? eg:(9)
# for i in range(1,5):
#     for j in range(1,1+i):
#         print(i,end=" ")
#     print()
  
# ?eg:(10)
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()    

#? eg:(11)
# for i in range(5, 0, -1):
#     for j in range(5, i - 1, -1):
#         print(j, end=" ")
#     print()

#? eg:(12)  -(Pyramid)
# for i in range(1,7):
#     for j in range(7-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")    
#     print()    

#? eg:(13)
# num=1
# for i in range(1,5):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()       



        
         

















