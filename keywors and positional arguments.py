#keywords and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
'''
'''def Details(id,name,mailid):
     print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="taruni",mailid="t@mail.com")
Details(30,"jyo",mailid="jyo@mail.com")
Details("harika","h@gmail.com",22)
Details(name="chandhana",mailid="c@mail.com",id=11)
Details(id,"name","mailid")'''

#default argument
'''def grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
grocery("sugar",100)'''

'''def grocery(item="rice",price=1333):
    print("item is %s" %item)
    print("price is %d" %price)
grocery()'''


'''def grocery(item,price=1333):
    print("item is %s" %item)
    print("price is %d" %price)
grocery("dhal")'''


'''def grocery(item="rice",price):
    #non-def arg follows def arg
    print("item is %s" %item)
    print("price is %d" %price)
grocery(333)'''

'''def bakery(item,price,qty):
    print("item is %s" %item)
    print("price is %d" %price)
    print("qty is %s" %qty)
bakery("black forest",900,"2kg")'''


#*star arguements
#used to unpack the elements
'''a=[2,3,4,5,6]
print(a)
print(*a)'''

'''a=(2,3,4,5,6)
print(a)
print(*a)
print(type(a))'''

'''a={2,3,4,5,6}
print(a)
print(*a)
print(type(a))'''

'''a={"year":2023,"month":3}
print(a)
print(*a)
print(type(a))'''

'''a,b,c=2,3,4,5,6,7,9,8,1,0
print(a)
print(b)
print(c)'''#error

'''a,*b,c=2,3,4,5,6,7,9,8,1,0
print(a)
print(*b)
print(c)'''

'''a,*b,*c=2,3,4,5,6,7,9,8,1,0
print(a)
print(*b)
print(*c)'''#error

a,*b,c="codegnan"
print(a)
print(*b)
print(c)

