#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7)
d=[5,6,7,8,9,10]
check(*d)
e={3,4,5,6,7}
check(*e)
f={"name":"taruni","city":"vij"}
check(*f)
'''
'''def check1(*a):
    d=2
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5,3.3,6.2,4.3)
check1(1,3,4,5,6.3,3.2,"taruni")'''

#kwargs(**)
'''def details(**a):
    print(a)
    print(type(a))
details()
d={"idnos":[10,20,30],
   "names":["taruni","harika","simha"],
   "status":["p","a","p"]}
details(**d)'''

'''def details(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
details()
d={"idnos":[10,20,30],
   "names":["taruni","harika","simha"],
   "status":["p","a","p"]}
details(**d)'''


#* and **
'''def details(*a,**b):
    d=3
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
details()
data=(2,3,4,5,2.3,4.5)
details(*data)
final={"names":["taruni","harika","simha"],
       "marks":[60,50,70]}
details(**final)
details(*data,**final)'''

#max,min,sum
'''print(max(4,6,8,9,10,20))
print(min(4,6,8,9,10,20))'''

'''a=2,3,4,5,6,7,8
print(sum(a))'''


