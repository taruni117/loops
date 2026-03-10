#funtions
#difference bwt functions and normal code
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''
'''a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''
#using functions
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''
#power,modulus,divison
'''def calculate(a,b):
    print("the pow is",a**b)
    print("the mod is",a%b)
    print("the intdiv is",a//b)
calculate(10,20)
calculate(55,22)'''

#runtime
'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
add()'''

'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''
#print vs return
'''def mul(a,b):
    print(a*b)
mul(3,4)'''

'''def mul(a,b):
    return a*b
print(mul(2,3))'''
 
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(3,4)'''

#return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return(c)
    #return(d)
    #return(e)
    return c,d,e
print(cal(2,4))'''

#task
'''def cal():
     a=int(input("a value"))
     b=int(input("b value"))
     option=int(input("choose the option 1.add 2.sub 3.mul"))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
    else:
        return "invalid value"'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
     b=int(input("b value"))
     option=int(input("choose the option 1.add 2.sub 3.mul"))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:'''
    
  

