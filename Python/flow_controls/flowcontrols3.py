 #!  _JUMPING STATEMENTS_ 
#!(1)BREAK STATEMENT
#? (upto 5, then break)
# i=1
# while i<=10:
#     print(i)
#     if i==5:
#        break
#     i+=1
    

#!(2)CONTINUE STATEMENT
# i=0
# while i<6:
#     i+=1
#     if i==3:
#         continue
#     print(i)
    

# i=0
# while i<=6:
#     if i==3:
#         i+=1
#         continue
#     print(i)
#     i+=1
        

#? 1-PROBLEM:PRINT NUM FROM 1 TO 20 USING A WHILE LOOP. STOP THE LOOP WHEN THE NUMBER BECOMES 12
# i=1
# while i<=20:
#     print(i)
#     if i==12:
#         break
#     i+=1


#? 2-PROBLEM:PRINT NUMBERS FROM 0 TO 15 USING A WHILE LOOP. SKIP PRINTING 8
# i=0
# while i<=15:
#     if i==8:
#         i+=1
#         continue
#     print(i)
#     i+=1
    

#! (3)PASS STATEMENT
# a=10
# b=15
# if a<b:
#     pass

#? 3-PROBLEM:USING WHILE LOOP PRINT 5 TO 40-->[5,10,15,20,25,30,35,40]
# i=5
# while i<=40:
#     print(i,end=",")
#     i+=5

#? 4-PROBLEM: PRINT 1 TO NUMBER(UPPER LIMIT)
# upperlim=int(input("Enter the upper lim:"))
# i=1
# while i<=upperlim:
#     print(i)
#     i+=1

#? 5-PROBLEM:PRINT FROM GIVEN LOWER LIM TO UPPER LIM
# i=int(input("Enter the lower limit:"))
# j=int(input("Enter the upper limit:"))
# while i<=j:
#     print(i)
#     i+=1    

#? 6-PROBLEM:SUM OF N NUMBERS
# n=int(input("Enter the nth number:"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#     i+=1
# print("SUM:",sum)

#? 7-PROBLEM:FACTORIAL OF A NUMBER
# num=int(input("Enter the number:"))
# fact=1
# i=1
# while i<=num:
#     fact*=i
#     i+=1
# print("Factorial:",s)

#? 8-PROBLEM:PRINT LOWER TO UPPER EVEN NUMBERS
# i=int(input("Enter the lower lim:"))
# j=int(input("Enter the upper lim:"))
# while i<=j:
#     if(i%2==0):
#         print(i)
#     i+=1

#? 9-PROBLEM:PRINT LOWER TO UPPER ODD NUMBERS
# i=int(input("Enter the lower lim:"))
# j=int(input("Enter the upper limit:"))
# while i<=j:
#     if i%2!=0:
#         print(i)
#     i+=1

#? 10-PROBLEM:PRINT EVEN NUMBERS AND ODD NUMBERS SUM FROM LOWER TO UPPER LIMIT
# i=int(input("Enter the lower lim:"))
# j=int(input("Enter the lower lim:"))
# even=0
# odd=0
# while i<=j:
#     if i%2==0:
#         even=even+i
#     else:
#         odd=odd+i
#     i=i+1
# print("Sum of even nums:",even)    
# print("Sum of odd nums:",odd)

#? 11-REVERSE A NUM USING WHILE LOOP
# num=int(input("Enter a number:"))    
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# print("Reverse of that num is:",rev)    

#? 12-CHECK WHETHER A NUM  IS PALINDROME
# num=int(input("Enter the number:"))
# original=num
# rev=0
# while num>0:
#     digit=num%10
#     rev=rev*10+digit
#     num=num//10
# if original==rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")         
#? ANOTHER METHOD
# num=input("Enter the number:")
# if num==num[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")    

#? 13-CHECK WHETHER A NUM IS PRIME OR NOT
# num=int(input("Enter num:"))   
# i=1
# count=0
# while i<=num:
#     if num%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print("Prime") 
# else:
#     print("Not prime")           




   


            

                        




