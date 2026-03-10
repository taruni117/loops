#list comprehension
a=["Codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]
'''for i in a:
    print(i.upper(),end=" ")'''
#syntax
#a=[expr for var in collection/range]
'''[i.upper() for i in a]
print(b)'''
'''print([i.upper() for i in a])'''
'''
a=["python","java","ml"]
b=[i.title() for i in a]
print(b)'''
#task sqaures 
'''a=[1,2,3,4,5,6,8,12,13]
b=[i*i for i in a]
b=[i**2 for i in a]
b=[pow(i,2) for i in a]
print(b)'''
#task with if condition in list comprehension
'''a=[i for i in range(20)if i%2==0]
print(a) '''#even 
    
'''a=[i for i in range(20)if i%2!=0]
print(a)'''#odd 

#even numbers to squares
'''a=[i*i for i in range(20)if i%2==0]
print(a)'''

#fruits only a letter word
'''fruits=["apple","grapes","mango","banana","kiwi","berry","dragon"]
a=[i for i in fruits if "a" in i]
print(a)'''

'''fruits=["apple","grapes","mango","banana","kiwi","berry","dragon"]
a=[i for i in fruits if "a"  not in i]
print(a)'''

#if else use in list comprehension
'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''
#task-output#6,6,6,6,6
'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
c=[a[i]+b[i] for i in range(5)]
print(c)''''





