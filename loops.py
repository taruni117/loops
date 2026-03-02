#loops()
#for loop(),while,range(),break(),continue(),pass()
#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)''' #prints output sequence
    
'''a=[10,20,30,40,50]
for i in a:
    print(i,end="")'''#give in parallel output

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''#this print how many times in a the output prints

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=(10,20,30,40,50)
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={10,20,30,40,50}
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name":"taruni","year":2026,"month":3}
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i)) #prints only keys
for i in a.values():
    print(i)
    print(type(a))#prints only values
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))#prints both
    print(type(i))'''

'''a="codegnan"
for i in a:
    print(i,end=" ")
    print(type(a))
    print(type(i))'''
#task
'''a=["code","python","course"]
for i in a:
    print(i.upper(),end=" ")'''

'''a=["code","python","course"]
b=str(a)
print(b.upper())'''

#while loop
'''a=10
while a>1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''
'''a=20
while a>=1:
    a=a-1
    print(a)'''

'''a=20
while a>1:
    a=a-1
print(a)'''

'''a=15
while a>2:
    print(a)
    a+=1'''
'''a=15
while a>=2:
    print(a)
    a-=1'''


'''a=3
while a<18:
    print(a)
    a*=1'''
#voting
'''while True:
    age=int(input("enter the age"))
    if age>=18:
        print("eligible for vote")
    else:
        print("not eligible for vote")'''
#social media
'''while True:
    username=input("enter the username")
    password=int(input("enter the password"))
    if username=="taruni" and password==1234:
            print("valid")
    else:
        print("invalid")'''
#bakery
'''while True:
    cake_price=int(input("enter the price"))
    if cake_price==1200:
        print("redvelvet cake")
    elif  cake_price==1000:
        print("chocolate cake")
    elif cake_price==800:
        print("butter scotch cake")
    elif cake_price==600:
        print("chop almond cake")
    else:
        print("sorry cake not available")'''


