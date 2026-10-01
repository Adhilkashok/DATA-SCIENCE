 #? CHECK WHETHER A NUMBER IS STRONG NUMBER OR NOT
#! A Strong Number is a number where the sum of the factorials of its digits equals the number itself.
#* Example
#* 145 is a Strong Number because:
#* 1! = 1
#* 4! = 24
#* 5! = 120
#* 1 + 24 + 120 = 145 ✅
# import math
# num=int(input("Enter a number:"))
# original=num
# sum=0
# while num>0:
#     digit=num%10
#     sum=sum+math.factorial(digit)
#     num=num//10
# if sum==original:
#     print(original,"is a Strong number")    
# else:
#     print(original,"is not a Strong number")


#? CHECK WHETHER A NUMBER IS ARMSTRONG NUMBER OR NOT
#! An Armstrong number is a number in which the sum of each digit raised to the power of the number of digits equals the original number.
#* Example: 153
#* 153 has 3 digits:

#* 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
# num=int(input("Enter a number:"))
# original=num
# sum=0
# a=len(str(num))
# while  num>0:
#     digit=num%10
#     sum=sum+digit**a
#     num=num//10
# if sum==original:
#     print("Armstrong")
# else:
#     print("Not Armstrong")      

#? CHECK A NUMBER IS AUTOMORPHIC OR NOT
#! A number is Automorphic if its square ends with the number itself.
#* Examples:
#* 5² = 25 → ends with 5 ✅
#* 6² = 36 → ends with 6 ✅
#* 25² = 625 → ends with 25 ✅
# num = int(input("Enter a number: "))
# sq=num*num
# if sq%(10**len(str(num)))==num:
#     print("Automorphic")
# else:
#     print("Not Automorphic")    

#? NEON NUMBER
#! A Neon number is a number where the sum of the digits of its square is equal to the original number.
#* Example:
#* 9² = 81
#* Add the digits:
#* 8 + 1 = 9
# num = int(input("Enter a number: "))
# sq=num*num
# sum=0
# while sq>0:
#     digit=sq%10
#     sum=sum+digit
#     sq=sq//10
# if sum==num:
#     print("Neon Number")    
# else:
#     print("Not Neon")

#? HARSHAD NUMBER(Niven Number)
#! A Harshad number is a number that is divisible by the sum of its digits.
#* Example:
#* 18
#* 1+8=9
#* 18 ÷ 9 = 2
# num=int(input("Enter a number:"))
# original=num
# sum=0
# while num > 0:
#     digit=num % 10
#     sum=sum + digit
#     num=num // 10
# if original % sum == 0:
#     print("Harshad Number")
# else:
#     print("Not a Harshad Number")

#? DUCK NUMBER
#! A Duck number is a number that contains at least one zero (0) in it, but the zero should not be at the beginning.
#* Examples
#* 102 → contains 0 → ✅ Duck Number
#* 1050 → contains 0 → ✅ Duck Number
#* 123 → no 0 → ❌ Not a Duck Number
#* 0123 → zero at the beginning → ❌ Not a Duck Number
# num=input("Enter the number:")
# if num[0]!="0" and "0" in num:
#     print("Duck number")
# else:
#     print("Not Duck number")    

#? PERFECT NUMBER
#! A Perfect Number is a number whose sum of its proper divisors (excluding the number itself) is equal to the original number.
#* Example: 
#* 6
#* The proper divisors of 6 are:
#* 1, 2, 3
#* Their sum:
#* 1 + 2 + 3 = 6
# num=int(input("Enter a number: "))
# sum=0
# i=1
# while i < num:
#     if num%i==0:
#         sum=sum+i
#     i=i+1
# if sum==num:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")

#? DEFINE A FUNCTION THAT TAKES A LIST AS AN ARGUMENT AND RETURNS A NEW LIST CONTAINING THE UNIQUE ELEMENTS FROM THE GIVEN LIST. THE ORDER OF ELEMENTS SHOULD BE MAINTAINED
#* EG:
#* input=[12,34,12,50,60]
#* output=[12,34,50,60]
# listt=[12,34,56,12,90,90,80]
# def unique(listt):
#     lst=[]
#     for i in listt:
#         if i not in lst:
#             lst.append(i)
#     return lst 
# print(unique(listt))       
       
#? PRINT ALL PRIME NUMBERS BTW 2 GIVEN NUMBERS.
# a=int(input("Enter the lower limit:"))
# b=int(input("Enter the upper limit:"))
# for i in range(a,b+1):
#     count=0
#     for j in range(1,1+i):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i,end=" ")        



#? 8. Shopping Bill with Discount-- Accept the purchase amount from the user.
#? Discount Rules:
#? Amount ≥ 5000 → 20% discount
#? Amount ≥ 2000 and < 5000 → 10% discount
#? Otherwise → No discount
#? Display:
#? Original Amount, Discount Amount, Final Amount
amount=float(input("Enter the purchase amount:"))
if amount>=5000:
    discount=(amount*20)/100
elif amount>=2000:
    discount=(amount*10)/100
else:
    discount=0
    print("No discount available")  
total_bill=amount-discount  
print("Original Amount:", amount)
print("Discount Amount:", discount)
print("Final Amount:", total_bill)    







