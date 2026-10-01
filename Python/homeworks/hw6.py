 #?(1):Write a recursive function to reverse a number.
# num=int(input("Enter a number:"))
# def rev_num(n,rev):
#     if n==0:
#         return rev
#     return rev_num(n//10,rev*10+n%10)
# print("Rverse is:",rev_num(num,0))

#?(2):Write a recursive function to count the number of digits in a number.
# num=int(input("Enter a number:"))
# def digits(n):
#     if n<10:
#         return 1
#     return 1+digits(n//10)
# print("No.of Digits is:",digits(num))

#?(3):Write a recursive function to check whether a string is a palindrome
# s=input("Enter a string:")
# def pali(s):
#     if len(s)<=1:
#         return True
#     if s[0]!=s[-1]:
#         return False
#     return pali(s[1:-1])
# if pali(s):
#     print("Palindrome")
# else:
#     print("Not palindrome")    

#?(4):Write a recursive function to calculate the sum of digits of a number
# num=int(input("Enter a number:"))
# def digit_sum(num):
#     if num==0:
#         return 0
#     return (num%10)+digit_sum(num//10)
# print("Sum of digits is:",digit_sum(num))

#?(5):Print the multiplication table of a number using recursion
# num=int(input("Enter a number:"))
# upper_lim=int(input("Enter the upper limit:"))
# def multi(num,i):
#     if i>upper_lim:
#         return
#     print(num,"x",i,"=",num*i)
#     multi(num,i+1)
# multi(num,1)    