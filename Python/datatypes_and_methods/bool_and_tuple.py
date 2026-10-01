 #! BOOL
# res=bool(20.5)
# res=bool(0)
# res=bool("apple")
# res=bool("")
# print(res)

# a=(1,2,3,"apple")
# a=(1,)
# a[3]="kiwi"
# print(a)
# print(type(a))

 #! TUPLE
#? PACKING
# a=(1,2,3,"apple")
# ? UNPACKING
# a=(1,2,3,"apple")
# (p,q,r,s)=a
# print("p:",p)
# print("q:",q)
# print("r:",r)
# print("s:",s)

 #! TUPLE METHOD
#? 1-COUNT()
# a=(1,2,3,"apple",2,2,4,2)
# res=a.count(2)
# res=a.count(7)

#? 2-INDEX()
# a=(1,2,3,"apple",2,2,4,2)
# res=a.index(2)
# res=a.index(24)
# print(res)

#* PROBLEM
#? CHANGE 10 TO 20
# tup=(23,34,10,5,9)
# lst=list(tup)
# lst[2]=20
# tu=tuple(lst)
# print(tu)