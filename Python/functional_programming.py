 #! __FUNCTIONAL PROGRAMMING__
#? PYTHON FUNCTIONS AS OBJECT
#* eg:
# def greet():
#     return "hello"
# data=greet
# print(data())

    #*or

# def greet():
#     return "hello"
# data=greet()
# print(data)    

#? FUNCTIONS AS ARGUEMENTS
#* eg:
# def greet():
#     print("Hello")
# def display(fun):
#     fun()
# display(greet)    

#! (1):LAMBDA FUNCTION==>SMALL ANONYMOUS FUNCION (a function witout a name)
#? syntax: 
   #! x=lambda arguments:expression
   #! print(x())
#? find square of a number
# x=lambda num:num*num
# print(x(12))

#? find the sum of 2 numbers
# sum=lambda a,b:a+b          # can use only one expression
# print(sum(20,30))

#? find product of 3 numbers
# prod=lambda a,b,c:a*b*c
# print(prod(2,3,6))
#? find cube of a number
# cube=lambda num:num**3
# print(cube(4))

#! (2):MAP FUNCTION==>APPLIES A FUNCTION TO EVERY ELEMENT IN AN ITERABLE(or list).
#? syntax:
    #! map(function,iterable)
#* eg:squares
# lst=[2,3,4,5]
# sq=list(map(lambda i:i*i,lst))     # use list funcion to get list as output
# print(sq)

#? find cube of each element:
# lst=[1,2,3,4,5,6,7]
# cube=list(map(lambda i:i**3,lst))
# print(cube)

#! (3):FILTER FUNCTION==>SELECTS ONLY THE ELEMENTS THAT SATISFIES A SPECIFIC CONDITION
#? syntax:
    #! filter(function,iterable)
#? find even numbers from the list
# lst=[1,2,3,4,5,6]
# res=list(filter(lambda i:i%2==0,lst))
# print(res)

#? print odd nums
# lst=[1,2,3,4,5,6,7,8,9]
# res=list(filter(lambda i:i%2!=0,lst))
# print(res)

#! (4):REDUCE FUNCTION:REDUCE ALL ELEMENTS TO A SINGLE VALUE
#? syntax:
    #! from functools import reduce
    #! reduce(function,iterable) 
#? find sum of the list
# lst=[1,2,3,4]
# from functools import reduce
# sum=reduce(lambda a,b:a+b,lst)
# print(sum)

#? find product of nums in a list
# lst=[1,2,3,4,5]
# from functools import reduce
# prod=reduce(lambda a,b:a*b,lst)
# print(prod)]

#! (5):ZIP FUNCTION==>COMBINING MULTIPLE ITERABLES
#? syntax:
    #! print(zip(lst1,lst2))
#* eg:
# names=["Adhil","Mishal"]
# age=[21,20]
# print(list((zip(names,age))))

#! (6):ENUMERATE FUNCTION==>RETURNS INDEX AND VALUE TOGETHER
#? syntax:
    #! for index,value in enumerate(lst)
#*eg:
# names=["Adhil","Rishal"]
# for index ,value in enumerate(names):
#     print(index,value)

#! (7):SORTED FUNCTION==>SORTS BASED ON STRING LENGTH
#? syntax:
    #! sorted(iterable,key=function)
#* eg:
# animals=["elephant","monkey","donkey","cat"]
# res=sorted(animals,key=lambda i:len(i))
# print(res)


#! (8):ANY FUNCTION==>RETURNS TRUE IF ATLEAST ONE VALUE IS TRUE
#* eg:
# num=[0,0,5,-1]                     
# print(any(num))

# 0       → False
# None    → False
# ""      → False
# False   → False
# Any non-zero number → True
# Non-empty string    → True

#! (9):ALL FUNCTION==>RETURNS TRUE IF EVRY VALUE IS TRUE
#* eg:
# num=[0,0,5,-1]
# print(all(num))


