# Q1 : ---------------------------------------------------------------
# l = [1,2,3,4,5,6,7,8]
# We have a even length of list.
# Condition :
# I do not want to waste any memory.No other variables are to be made.All the changes are to be done in the same list "l"Also you cannot use any kind of loop.
# Expected Output :
# l = [1,2,3,4,5,6,7,8]
# o/p [1,5,2,6,3,7,4,8]

'''
l = [1,2,3,4,5,6,7,8]
x = len(l)//2  
l[::2],l[1::2] = l[:x],l[x:] 
print(l)'''
# x = (l[0:-1:4],l[1:-1:4],l[2:-1:4],l[3:9:4])
# y = []
# for i in x:
#     for j in i:
#         y.append(j)
# print(y)        


#Q2 :  Condition : You cannot create any another variable and have to sort this dictionary by the value. All the changes are to be made on this dictionary only.
'''d = {
  "a" : 10,
  "b" : 30,
  "c" : 40,
  "d" : 20,
}

d =dict(sorted(d.items(), key = lambda x : x[1]))
print(d)
'''

#  ================= ISINSTANCE =================================

# name = "viplove"
# print(isinstance(name,str))

# a = 10
# b = 10.5
# c = "hello"
# d = [1, 2, 3]
# e = (1, 2, 3)
# f = {1, 2, 3}
# g = {"name": "Viplove"}

# print(isinstance(a,int))
# print(isinstance(b,float))
# print(isinstance(c,str))
# print(isinstance(d,list))
# print(isinstance(e,tuple))
# print(isinstance(f,set))
# print(isinstance(g,dict))

'''# ...TYPE-OFF-------------------------------------------------'''
# print(type(f) == set)
# print(type(a)==int)
# print(type(b) == float)
# print(type(c) == str)
# print(type(d) == list)
# print(type(e) == tuple)
# print(type(f) == set)
# print(type(g) == dict)

# isinstance in oop  ---------------------------------------------
# class Animal:
#     print("animal class")
# class Plane:
#     pass    
# class Dog(Animal):  
#     pass
# obj = Dog()
# print(isinstance(obj,Dog))
# print(isinstance(obj,Animal))
# print(isinstance(obj,object))
# print(type(int))
# print(type(None))

# x = 10
# print(isinstance(x,object))
# print(isinstance(x,(int,float)))
# x = 10.5
# print(isinstance(x,(int,float)))
# x = "10"
# print(isinstance(x,(int,float))) #// False


# def checkdata(x):
#     if isinstance(x,int):
#         print("integer")
#     elif isinstance(x,float):
#         print("Float")
#     elif isinstance(x,str):
#         print("string")
#     else:
#         print("other type")
# checkdata(10)                            
# checkdata(10.5)                            
# checkdata("viplove") 


'''def check(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a+b
    return "only integers alloewd"
print(check(10,"20"))'''


def recursive(number):
    flatten = []
    for i in number:
        if isinstance(i):
            flatten.extend(recursive(i))
        else:
            flatten.append(i) 
    return flatten           
l = [[1,2,[10,12],0,],[[13,14,15,[7,77,[90,50]]],3,4],[5,6]]   
print(recursive(l))   

    
                            
  





