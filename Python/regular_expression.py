 #! __REGULAR EXPRESSION__
#? input mail whether it is valid or not
# mail=input("Enter mail id:")
# if "@" in mail and "." in mail:    #gives valid when more thn 1 @ comes, but actually it is not valid
#     print("Valid")
# else:
#     print("Not Valid")

#! MODULE USED ==>re
import re
#? (1)MATCH()-->Checks only the beginning of string
# text="python is fun"
# res=re.match("python",text)
# print(bool(res))          #bool is used to get the output as true or false.

#? (2)SEARCH()-->Searches pattern anywhere in the string
# text="python is fun"
# res=re.search("is",text)
# print(bool(res)) 

#? (3)FINDALL()-->Returns all matches as a list
# text="python is python fun python"
# print(re.findall("python",text))

#? (4)FINDITER()-->Returns the starting and ending index of a word
# text="python java python c"
# for i in re.finditer("python",text):
#     print(i.start(),i.end())

#? (5)SUB()-->Replaces matched text 
# text="i love python"
# res=re.sub("python","java",text)
# print(res)

#? (6)SPLIT()-->Splits the given text in a list
# text="apple,orange,mango"
# res=re.split(",",text)
# print(res)
           
# text="apple,orange;mango banana"
# print(re.split("[,; ]",text))


#! REGEX SPECIAL CHARACTERS
#? 1)DOT(.)
#* eg:
# print(re.findall("c.t","cat c9t cpk dog"))
#* eg:
# print(re.findall("c..t","caat c9t cpk dog"))

#? 2)CARET(^)-->Returns if the word is present in the beg of the string
#* eg:
# print(re.findall("^pyth","python is easy"))

#* eg:
# print(re.findall("^is","python is easy"))

#? 3)DOLLAR($)-->Returns if the word is present in the end of the string
#* eg:
# print(re.findall("fun$","python is fun"))



#! CHARACTER CLASSES
#? 1)[abc]-->Matches either a,b or c
# print(re.findall("[abc]","apple bat cat"))

#? 2)[0-9]-->Digits
# print(re.findall("[0-9]","abc12345"))

#? 3)[^0-9]--> Any character except [0-9]
# print(re.findall("[^0-9]","abc1234"))

#? 4)[a-z]-->Reads lower case
# print(re.findall("[a-z]","AbcdeF1234"))

#? 5)[A-Z]-->reads upper case
# print(re.findall("[A-Z]","AbcdEf1234"))

#? 6)[a-zA-z]-->Reads both cases
# print(re.findall("[a-zA-Z]","AbcdEf1234"))



#! PREDEFINED CHARACTER CLASS
#? SYMBOLS      |         MEANING

# \d            |         digits(0-9)
# print(re.findall(r"\d","abcd1123"))


# \D            |         not a digit
# print(re.findall(r"\D","abcd1123"))


# \w            |         letters,digits,underscores
# print(re.findall(r"\w","abcd11_23"))


# \W            |         not a word character
# print(re.findall(r"\W","ab@cd11 2#3"))


# \s            |         whitespaces
# print(re.findall(r"\s","abcd 1123"))


# \S            |         not whitespaces
# print(re.findall(r"\S","abcd 11@23"))


#? Write a program to find the sum of the digits of a given number
# import re
# num=input("Enter the digits:")
# total=sum(map(int,re.findall(r"\d",num)))
# print(total)


#! QUANTIFIERS==>SPECIFIES HOW MANY TIMES A CHARACTER OR GROUP APPEAR
#? 1) * ==>ZERO OR MANY TIMES THE PRECEEDING CHARACTER
#* eg:
#? ba*==>b,ba,baaa,....
# print(re.findall("ab*","a abb abc abbb bb"))

#? 2) + ==>ONE OR MANY TIMES THE PRECEEDING CHARACTER
# print(re.findall("ab+","a ab abc abbb bb"))

#? 3) ? ==>ZERO OR ONE(optional)
# print(re.findall(r"colou?r","color,colour"))

#? 4) {n} ==>EXACTLY n TIMES
# data="12 123 1234 12345"
# print(re.findall(r"\d{3}",data))

#? 5) {n,m} ==>BETWEEN N AND M
# data="12 123 1234 123456 123456789"
# print(re.findall(r"\d{2,4}",data))

#? 6){n,} ==>ATLEAST n ITEMS
# data="12 123 1234 12345"
# print(re.findall(r"\d{3,}",data)) 


#* PROBLEMS:
#? VALIDATE MOBILE NUMBER
# import re
# mobile_num=input("Enter the mobile number:")
# pattern=(r"^(\+91[\s-]?)?[6-9]\d{9}$")
# if re.match(pattern,mobile_num):
#     print("Valid")
# else:
#     print("Not valid")    

#TODO ( \d+ ) => Matches digits together
# data="apple costs 120 orange costs 80"
# print(re.findall(r"\d+",data))

#TODO ( \w+ ) => Matches digits,characters,underscores together
# data="apple costs 120 orange_costs 80"
# print(re.findall(r"\w+",data))

#? 1. Count how many digits are present in a string.
# import re 
# text=input("Enter the string:")
# digits=re.findall(r"\d",text)
# print(len(digits))

#? 2. Extract all email IDs from a paragraph.
# import re
# text = input("Enter the paragraph: ")
# emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
# print("Email IDs:")
# for email in emails:
#     print(email)

#? 3. Validate a password (minimum 8 characters, at least one uppercase, one lowercase, one digit, and one special character).
# import re
# password = input("Enter password: ")
# pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$"
# if re.match(pattern, password):
#     print("Valid Password")
# else:
#     print("Invalid Password")

#? 4. Remove all special characters from a string.
# import re
# text = input("Enter a string: ")
# result = re.sub(r"[^a-zA-Z0-9 ]", "", text)
# print(result)

#? 5. Find all words starting with a capital letter.
# import re
# text = input("Enter a sentence: ")
# words = re.findall(r"\b[A-Z][a-zA-Z]*\b", text)
# print(words)

#? 6. Extract all dates in DD-MM-YYYY format.
# import re
# text = input("Enter text: ")
# dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)
# print(dates)
#? 7. Count the number of vowels using regex.
# import re
# text = input("Enter a string: ")
# vowels = re.findall(r"[aeiouAEIOU]", text)
# print("Number of vowels:", len(vowels))

#? 8. Replace multiple spaces with a single space.
# import re
# text = input("Enter a sentence: ")
# result = re.sub(r"\s+", " ", text)
# print(result)

#? 9. Validate a vehicle registration number like KL13AB1234.
# import re
# vehicle = input("Enter vehicle number: ")
# pattern = r"^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$"
# if re.match(pattern, vehicle):
#     print("Valid Vehicle Number")
# else:
#     print("Invalid Vehicle Number")






















