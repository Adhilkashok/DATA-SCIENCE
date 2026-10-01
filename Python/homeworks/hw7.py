 #?(1): Create a module message.py with a function greet(name) then Import and call the function
# import message
# name=input("enter your name: ") 
# message.greet(name)

#?(2):Create a module number.py with functions:even_odd(n) square(n) Import the module and use both functions.
# import ev_odd_sq
# num=int(input("Enter a number:"))
# ev_odd_sq.even_odd(num)
# ev_odd_sq.square(num)



# TODO-NESTED LIST;
#? (1):Given:numbers = [[2, 4, 6],[8, 10, 12],[14, 16, 18]]
#? Print:10,18,6
# numbers = [[2, 4, 6],[8, 10, 12],[14, 16, 18]]
# print(numbers[1][1])  
# print(numbers[2][2])  
# print(numbers[0][2]) 

#?(2):Given a nested list of integers, count how many even numbers are present.
#? Example:matrix = [[1, 2, 3],
#?                   [4, 5, 6],
#?                 [7, 8, 9]]
# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# count=0
# for row in matrix:
#     for num in row:
#         if num%2==0:
#             count+=1
# print("even numbers are:",count)        

#? (3):Print Row-wise Sum
#? Given:
#? matrix = [
#?     [2, 3],
#?     [4, 5],
#?     [6, 7]
#? ]    
# matrix = [
#     [2, 3],
#     [4, 5],
#     [6, 7]
# ]   
# for row in matrix:
#     total=0
#     for num in row:
#         total+=num
#     print(total)    

#? (4):Write a program to find the largest number in a nested list.
# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# largest=matrix[0][0]
# for row in matrix:
#     for num in row:
#         if num>largest:
#             largest=num
# print("Largest number is:",largest)            

#? (5):Given: matrix = [[1, 2, 3],[4, 5, 6]]. Find and print the sum of all elements.
# matrix = [[1, 2, 3],[4, 5, 6]]
# total=0
# for row in matrix:
#     for num in row:
#         total+=num
# print("sum is:",total)        







