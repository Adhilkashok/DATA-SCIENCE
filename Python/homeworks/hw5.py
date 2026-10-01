 #?(1): write a function to print the multiplication table of 7(M1).
# def mt():
#     for i in range(1,15):
#         print("7 x",i,"=",7*i)
# mt()        

#?(2):Wrie a funcion that accepts a string and returns the no of vowels in it(M3).
# text=input("Enter a string:")
# def count_vow(s):
#     count=0
#     for ch in s:
#         if ch.lower() in "aeiou":
#             count+=1
#     return count
# result=count_vow(text)
# print("No of vowels:",result)       

#?(3):Write a funcion that accepts a list of integers and print all +ve nums(M2).
# num=[-2,0,-3,1,2,3,4]
# def positive(lst):
#     for i in lst:
#         if i>0:
#             print(i)
# positive(num)  

#?(4):Accept a number and print its reverse(M2).
# n=int(input("Enter a number:"))          
# def reverse(num):
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     print("Reverse:",rev) 
# reverse(n)       

#?(5):Acceot a list and return the avg of its elements(M3).
# num=[10,20,30,90,40]
# def average(lst):
#     s=0
#     for i in lst:
#         s+=i
#     avg=s/len(lst)
#     return avg
# result=average(num)
# print(result)    
