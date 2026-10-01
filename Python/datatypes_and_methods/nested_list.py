 #! _NESTED LIST_
# lst=[[1,2,3],[4,5,6]]
# print(lst[0])
# for i in lst:
#     print(i)
#     print(i[1:3])

#? PROBLEM:EMPLOYEE DETAILS;  ID,FNAME,LNAME,AGE,PROF,LOC,SALARY
#? 1) find id,fname,lname ,age,prof,loc of employees where age>25
#? 2) age==27, fname,lname,age
#? 3)python prof--> fname,lname,age,loc
#? 4) age above 24 ,prof python return full details
#? 5)find total salary of all employees
employees=[[1,"adhil","k",22,"datascience","perambra",10000],
           [2,"rishal","av",27,"python","vadakara",20000],
           [3,"mishal","m",21,"datascience","ulliyeri",15000],
           [4,"anshin","r",25,"fullstack","marutheri",25000],
           [5,"rohith","r",22,"datascience","calicut",35000],
           [6,"rishi","s",20,"datascience","ulliyeri",55000],
           [7,"dilsha","d",21,"fullstack","perambra",45000]]
#? 1st answer
# for i in employees:
#     if i[3]>25:
#         print(i[0:6])

#? 2nd answer
# for i in employees:        
#     if i[3]==27:
#         print(i[1:4])  

#? 3rd answer
# for i in employees:
#     if i[4]=="python":
#         i.remove(i[4])
#         print(i[1:5])

#? 4th answer
# for i in employees:        
#     if i[3]>24 and i[4]=="python":
#         print(i)   

#? 5th answer
# total=0
# for i in employees:
#     total=total+i[6]
# print(total)
        
     

        

           
