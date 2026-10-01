 #?(1):Given:
#?numbers = [5, 10, 15, 20, 25] 
#? Create a new list where each number is multiplied by 3.
# numbers = [5, 10, 15, 20, 25]
# new_lst=[i*3 for i in numbers]
# print(new_lst)

#?(2): names = ["Anu", "Arjun", "Diya", "Akhil", "Rahul"]
#? Create a list containing only the names that start with "A".
# names = ["Anu", "Arjun", "Diya", "Akhil", "Rahul"]
# new_lst=[i for i in names if i.startswith("A")]
# print(new_lst)

#?(3): Create a list of numbers from 1 to 100 that are divisible by both 3 and 5.
# lst=[i for i in range(1,101) if i%3==0 and i%5==0]
# print(lst)

#?(4):Given
#? sentence = "Data Science with Python"
#? Create a list containing only the vowels from the sentence.
# sentence = "Data Science with Python"
# lst=[i for i in sentence if i.lower() in "aeiou"]
# print(lst)

#?(5):numbers = [2, 5, 8, 11, 14]
#? Create a list where:
#? If the number is even, multiply it by 10.
#? Otherwise, multiply it by 100.
# numbers = [2, 5, 8, 11, 14]
# lst=[ i*10 if i%2==0 else i*100 for i in numbers]
# print(lst)
