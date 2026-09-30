# no arguments,no return values
'''def greet():
   print("hello")
greet()'''

# argument, no return values
'''def sum(a,b):
    print(a+b)
sum(1,2)
'''

# no arguments,return value 
'''def greet():
    print("hi")
    return "viplove"
res=greet()
print(res)'''

# arguments, return value 
'''def sum(a,b):
    return a+b
res = sum(10,20)
print(res)
'''

# TYPES OF ARGUMENT---------------------------------------
# positional argument

'''def positional(name,age):
    print(name,age)
positional("viplove",24)   ''' 

# keyword argument

'''def keyword(name,age):
    print(name)
    print(age)
keyword(age=24,name = "viplove")  '''  

# default argument

'''def default(name,age=24):
    print(name)
    print(age)
default("viplove")    '''

# variable length positional argument

'''def func(*args):
    print(args)
func(10,20,30,40) 
'''
'''def func(*args):
    total = 0
    for i in args:
        total+=i
    print(total)       
func(1,2,3,4,5,6) '''

# variable length keyword argument

'''def func(**kwargs):
    print(kwargs)
func(name = "viplove",age = 24,city = "dews")
'''

'''def func(*args, **kwargs):
    print(args,kwargs)
func(10,20,30,40,name = "viplove",city= "dewas") '''

'''def func(*args, **kwargs):
    print(2*2)
func() '''


# SCOPE --------------------------------------------------------------------------------
'''
def scope():
    name = "viplove"
    print(name)
scope()    
    '''

# name = "viplove"
# def scope():
#     print(name)
# scope()


'''def scope():
    name = "viplove"
scope()'''

# GLOBAL SCOPE----------------------------------------------
'''
x = 100
def func():
    x =200
    print(x)
func()  
print(x) ''' 


'''x = 100
def func():
    global x
    x =200
func()
print(x)
'''

'''def outer():
    name = "viplove"
    def inner():
        print(name)
    inner()    
outer()'''

# LEGB
# name = "rohan"
# def outer():
#     global name
#     name = "viplove"
#     def inner():
#         nonlocal name 
#         name = "sana"
#     inner()  
#     print(name, "inner")  
# outer() 
# print(name ,"outer")


