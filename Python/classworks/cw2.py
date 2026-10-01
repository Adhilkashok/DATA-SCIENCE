 #? 1. Write a Python function that takes a string as input and returns a dictionary containing the frequency(count) of each character in the string.The characters should be used as keys and their occurrence counts as values.Ignore all space characters while counting.Example:Input:"hello world"Output: {'h': 1,e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
# text=input("Enter a string:")
# def char_freq(s):
#     d={}
#     for ch in s:
#         if ch==" ":
#             continue
#         if ch in d:
#             d[ch]+=1
#         else:
#             d[ch]=1
#     return d
# result=char_freq(text)           
# print(result) 



#? 2. print the pattern
#? p
#? py
#? pyt
#? pyth
#? pytho
# num="python"
# for i in range(1,6):
#     print(num[:i])    

#? 3. Write a program to print the following pattern
#? 1
#? 2  3
#? 4  5  6
#? 7  8  9  10
# 11  12  13  14  15
# num=1
# for i in range(1,6):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1    
#     print() 