 #! EXCEPTION HANDLING
#  ------------------------------------
# division
# a=25
# b=0
# print(a/b) --> zero division error
# age=rahul --> value error

#? Try and Except => Try and Except are used for exception handling, allowing your program to handle errors gracefully instead of crashing.
#? Try:
#*     code that may raise an error
#? except:
#*     code to execute when error occur

#? eg:
# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print("Zero division not possible")    

# try:
#     a=10
#     b=0
#     print(a/b)
# except Exception as e:
#     print("error",e)

try:
    age=int(input("Enter age:"))
    print("age =",)    
except Exception as e:
    print("error",e)    


        

