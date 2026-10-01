  #! FILE HANDLING/FILE OPERATIONS 
#? CREATING NEW FILE:
# file=open("adhil123.txt","x")
# print("file created successfully")
# file.close()

#? ADDING CONTENT
# f=open("adhil123.txt","a")
# f.write("Adhil")
# print("added data successsfuly")
# f.close()

#? READING FILE(reading the data)
# f=open("adhil123.txt","r")
# data=f.read()
# print(data)
# f.close()

#? APPEND (adding new data to next line)
# f=open("adhil123.txt","a")
# f.write("\nMishal")
# print("added successfully")
# f.close()

#? Writing a data
# f=open("adhil123.txt","w")
# f.write("Adhil K Ashok")
# f.close()



#? WRITING MULTI LINES
#? METHOD(1):USING WRITE
# f=open("adhil123.txt","w")
# f.write("Adhil K Ashok")
# f.write("\nRishal")
# f.close()

#? METHOD(2):USING LIST
# students=["Adhil\n","Rishal\n","Mishal"]
# f=open("adhil123.txt","w")
# f.writelines(students)           # writelines=for multiple strings
# f.close()


#? WITH -CONTEXT MANAGER(with=>automatically closes the file,even if an error occurs.)
# with open("adhil123.txt","r") as f:
#     print(f.read())

#? APPEND USING WITH
# with open("adhil123.txt","a") as f:
#     f.write("\nNesla")

#? TAKING USER INPUT
# name=input("Enter a name:")
# with open("adhil123.txt","a") as f:
#     f.write("\n"+name)
# print("added successfully")

    
#? FILE HANDLING FROM OUTSIDE THE DIRECTORY  
# with open(r"C:\Users\adhil\OneDrive\Desktop\demo.txt","r") as f:         
#     print(f.read())

#? WRITING LIST OF NUMBERS
# num=[1,2,3,4,5,6,7]
# with open("numbers123.txt","w") as f: 
#     f.writelines(str(num))                  #-->write() can only write strings,not lists.


#? CREATE A LIST BY ADDING THE NUMBERS ,THEN FIND ITS SUM
# with open("list123.txt","x") as f:
#     pass
#? another method
# lst=[]
# n=int(input("Enter total nums needed:"))
# for i in range(n):
#      num=int(input("Enter a number:"))
#      lst.append(num)
#      with open("list123.txt","w") as f:
#           f.writelines(str(lst))
# print("List:",lst)
# print("Sum:",sum(lst))

#?another method
# numbers=[10,20,30,40,50]
# total=sum(numbers)
# print("List:",numbers)
# print("Sum:",total)


#? PROBLEM:COUNT THE FREQUENCY OF EACH WORD IN THE FILE
# with open(r"C:\Users\adhil\OneDrive\Desktop\vs.txt","r") as f:
#     dic={}
#     for i in f:
#       data=i.split()
#       for j in data:
#         if j not in dic:
#           dic[j]=1
#         else:
#            dic[j]+=1
# print(dic)           



#? PROBLEM:
#? (1):Dancer prof, frame, Iname
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#         # print(lst)  
#     for j in lst:
#         if j[4].lower()=="dancer":  
#           print(j[1:3])
    
#? (2):Age above  23  fname, lname, age, prof
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if int(j[3])>23:
#             print(j[1:5])

#? (3):Age range 25 to 40 fname. Iname, age, prof
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if int(j[3])>=25 and int(j[3])<=40:
#             print(j[1:5])

#? (4):india work, fname, Iname, age, prof
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if j[5].lower()=="india":
#             print(j[1:5])
    
#? (5):india work and age above 38 fname. lname, age

# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if j[5].lower()=="india" and int(j[3])>38:
#             print(j[1:4])

#? (6):india work and pro Dancer frame. lname, age
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if j[5].lower()=="india" and (j[4]).lower()=="Dancer":
#             print(j[1:4])

#? (7):Pilot prof frame. Iname, age
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if j[4].lower()=="pilot":
#             print(j[1:4])

#? (8):Pilot prof and age above 40 fname, lname, age
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if j[4].lower()=="pilot" and int(j[3])>40:
#             print(j[1:4])

#? (9):us work fname, name, age
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if j[5].lower()=="usa":
#             print(j[1:4])

#? (10):us work and age above 45 frame. lname, age
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
#     # print(lst)   
#     for j in lst:
#         if j[5].lower()=="usa" and int(j[3])>45:
#             print(j[1:4])
          
#? (11):Each profession count
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
# dic={}  
# for j in lst:
#     profession=j[4]
#     if profession not in dic:
#         dic[profession]=1
#     else:
#         dic[profession]+=1
# print(dic)            
       
#? (12):Each Location count
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
# dic={}  
# for j in lst:
#     location=j[5]
#     if location not in dic:
#         dic[location]=1
#     else:
#         dic[location]+=1
# print(dic)  

#? (13):Each Age group count
# with open(r"C:\Users\adhil\OneDrive\Desktop\employees.txt","r") as f:
#     # f.read()
#     lst=[]
#     for i in f:
#         lst.append(i.strip().split(","))
# dic={}  
# for j in lst:
#     age_grp=j[3]
#     if age_grp not in dic:
#         dic[age_grp]=1
#     else:
#         dic[age_grp]+=1
# print(dic)







