 #? create a list containing numbers from 1 to 50
# lst=[]
# i=1
# while i<=50:
#    lst.append(i)
#    i+=1
# print(lst)

   #*or

# lst=[]
# for i in range(1,51):
#     lst.append(i)
# print(lst)    



#! LIST COMPREHENSION
#? General syntax:
#! new_lst=[expression for item in iterable]
#* eg:
# lst=[i for i in range(1,51)]
# print(lst)
#* eg:
# lst=[i for i in "python"]
# print(lst)

#?create a list of squares of numbers from 1-10
# lst=[i**2 for i in range(1,10)]
# print(lst)

#?create a list of cubes of numbers from 10 to 15
# lst=[i**3 for i in range(10,16)]
# print(lst)

# ?
# lst=[i.upper() for i in "python"]
# print(lst)

# ?
# fruits=["apple","orange","mango","pineapple"]
# fru=[len(i) for i in fruits]
# print(fru)

#! LIST COMPREHENSION WITH CONDITION - (IF CONDITION)
#? syntax:
#! lst=[expression for item in iterable if condition]
#* eg:
# lst=[i for i in range(1,11) if i%2==0]
# print(lst)
#* eg:
# lst=[i for i in range(1,21) if i%2!=0]
# print(lst)

#! if-else condition
#?syntax:
#! lst=[expression1 if conndition1 else expresssion2 for item in iterable]
#* eg:
# lst=[ "even" if i%2==0 else "not even" for i in range(1,11)]
# print(lst)
# ?
# marks=[18,29,48,23,9]
# res=["pass" if i >13 else "fail" for i in marks]
# print(res)
   

#? (1):Create a new list containing the squares of all even numbers from 1 to 20 using list   comprehension.
#? Expected Output:
#? [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
# new_lst=[i**2 for i in range(1,21) if i%2==0]
# print(new_lst)

#? (2).Given the following list:
#? words = ["apple", "banana", "kiwi", "grape", "orange", "fig"]
#? Using list comprehension,create a new list containing only the words whose length is greater than 4.
#? Expected Output:
#? ["apple", "banana", "grape", "orange"]
# words = ["apple", "banana", "kiwi", "grape", "orange", "fig"]
# new_lst=[i for i in words if len(i)>4]
# print(new_lst)

#? Create a list of squares of all even nums from 10 -50
# lst=[i**2 for i in range(10,51) if i%2==0]
# print(lst)



