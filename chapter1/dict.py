
'''a = {
    "name":"viplove",
    "age":23,
    "email":"viplovesana90@gmail.com",
    "city":"dewas"
    }
print(a["name"])
print(a.get("city"))'''


# Adding and Updating Dictionary Item

'''a["marks"] = 80 # @adding items
print(a)
print(a.get("marks"))
print(a["marks"])

a["email"] = "viplove@123" #updating items
print(a)

# deleting itwms------

del a["marks"]
print(a)
'''


# student = {
#     "name":"viplove",
#     "email":"viplovesana90@gmail.com",
#     "city":"dewas"
#     }

'''student["age"] = 23
student["city"] = "indore"
print(student)'''
'''print(student)

student.update({"name":"viplove sana",
                "city":"indore",
                "age":24})
print(student)'''

# POP method---------------------

'''x = student.pop("email")
print(x)
print(student)'''

'''
x = student.popitem() #to remove last item from the dict
print(x)
print(student)'''

''''x = student.clear() #clear everything
print(x)
print(student)'''

# --METHODS OF DICTIONARY----------------


# student = {
#     "name":"viplove",
#     "email":"viplovesana90@gmail.com",
#     "city":"dewas"
#     }

# x = student.get("name")
# print(x)

'''x = student.keys()
print(x)
x = student.values()
print(x)'''
'''x = student.items()
print(x)'''
# x = student.keys()
# print(x)

# for loop in dictionaries--------------------------------

# student = {
#     "name":"viplove",
#     "email":"viplovesana90@gmail.com",
#     "city":"dewas"
#     }
'''for value in student.values():
    print(value)'''
'''for keys in student.keys():
    print(keys)'''
# print(student.keys())

'''for key,value in student.items():
    print(key,value)
'''


# in operator-----------------------------

'''print("name" in student)
print("email" in student)
print("code" in student)'''

'''# /cheaking from the values bcs "in" does not work on values
print("viplove" in student)
print("viplove" in student.values())'''

# print(len(student))


'''student = {
    "name":"viplove",
    "email":"viplovesana90@gmail.com",
    "city":"dewas",
    "name" : "rohan" # last value of same same key can overeright
    }
print(student)'''

# ---NESTED DICTIONARIES------------------------

# student = {
#     "student1":{
#            "name":"viplove",
#             "email":"viplovesana90@gmail.com",
#             "city":"dewas"
#     },
#     "student2":{
#              "name":"rohan",
#               "email":"rohan0@gmail.com",
#               "city":"indore"   
#     }
# }
'''x = (student["student1"]["name"])
y = (student["student2"]["email"])
print(x)
print(y)'''
'''for key,value in student.items():
    print(key,value["name"])'''

# Dictionary + List--------------------------------

# students = [
#     {"name":"viplove","city":"dewas"},
#     {"name":"rohan","city":"indore"},
#     {"name":"krish","city":"bhopal"}
# ]
# # print(students)
# print(students[0]["name"])

# ----Copy od dictionaries----------------------

'''a = {
    "name": "Viplove",
    "age": 23
}
b = a.copy()
b["age"] = 24
print(a)
print(b)'''

# ----------setdefault  in dictionaries-------------

'''student = {
    "name":"viplove"
}

x = student.setdefault("city","indore")
print(x)
print(student)
'''

'''keys = ["name","age","city"]
x = dict.fromkeys(keys,"viplove")
print(x)
    '''


# Dictionary comprehension------------------------

'''square = {}
for i in range(1,11):
    square[i] = i*i
print(square)  ''' 

'''a = [1,2,3,4,3,2,5,6,5,7,8,6,7]
new = {}
for i in a:
    if i in new:
        new[i] += 1
    else:
        new[i] =1
print(new)            '''

'''square = {i:i*i for i in range(1,6)}
print(square)'''

# Dictionary comprehension with condition

'''res = {i:i*i for i in range(1,11) if i%2==0}
print(res)
'''
'''
marks = {
    "math": 50,
    "science": 60,
    "english": 70
}
marks["english"] += 10 #static
print(marks)

for sub in marks:
    marks[sub] += 10 #dynamic
print(marks)    
    '''

# find the maximum marks ---------------------------------------------------

'''marks = {
    "math": 80,
    "science": 95,    
    "english": 70
}
maximum = 0 
for subject in marks:
    if marks[subject] > maximum:
        maximum = marks[subject]
        res = maximum
print(maximum)   '''     

'''marks = {
    "math": 80,
    "science": 95,    
    "english": 70
}
maximum = 0
x = ""
for key,value in marks.items():
    if value > maximum:
        maximum = value           
        x = key
print(x)        
print(maximum)   '''

# marks = {
#     "b": 80,
#     "a": 95,    
#     "c": 70
# }
# x = dict(sorted(marks.items()))
# print(x)

# find the maximum marks ---------------------------------------------------

'''marks = {
    "math": 50,
    "science": 95,    
    "english": 70
}
value = list(marks.values())
minimum = value[0]
for key,value in marks.items():
    if value < minimum:
        minimum = value
   
  
print(minimum)'''  

student = {
    "name": "Viplove",
    "age": 23,
    "course": "Python"
}
# x = student["name"]
# print(x)
# x = student.values()
# print(x)

# student["age"] = 24
# print(student)

# student["city"] = "bhopal"
# print(student)

# print('email' in student)

# print(len(student))
# print(len(student.keys()))
# print(student.keys())
# print(student.values())

# for key,value in student.items():
#     print(key,"=",value)
'''
marks = {
    "math": 80,
    "science": 90,
    "english": 75
}'''

'''total = 0
for key,value in marks.items():
    total = total + value
print(total)  '''  

# Average marks-------------------------------------------------
'''
total = 0
avg = 0
for value in marks.values():
    total += value
avg = total/len(marks.values())
print(avg)
 '''

# Maximum values-----------------------------------------------

'''maximum = 0

for value in  marks.values():
    if value > maximum:
        maximum = value
print(maximum)  '''      


'''maximum = 0
maxkey = " "
for key,value in  marks.items():
    if value > maximum:
        maximum = value
        maxkey = key

print(maxkey,"=",maximum)   '''  



'''marks = {
    "math": 80,
    "science": 20,
    "english": 99
}

minimum = list(marks.values())[0]

# minikey = list(marks.keys())


for key,value in  marks.items():
    if value < minimum:
        minimum = value
        if value == minimum:
            minikey = key

print(minimum,minikey)''' 

# Q14. 60 se greater marks
'''
marks = {
    "math": 50,
    "science": 95,
    "english": 70,
    "hindi": 45
}'''

'''for key,value in marks.items():
    if value > 60:
        print(key,"=",value)'''
'''
a = ["apple", "banana", "apple", "orange", "banana", "apple"]

new = {}
for i in a:
    if i in new:
        new[i] += 1
    else:
        new[i] = 1
for key,value in new.items():
    print(key,":",value)           
       '''
  
# Q17. Duplicate values find karo
'''a = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
empty_list = []
for value in a.values():
    empty_list.append(value)
d = {}    
for i in empty_list:
    if empty_list.count(i) > 1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
print(d)                
     '''

# Q18. Unique values
'''
# Same dictionary se sirf unique values print karo.

a = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}    
list = []
for key,value in a.items():
    list.append(value)
x = set(list)
print(x)'''


# Q20. Two dictionaries merge karo
'''a = {"name": "Viplove", "age": 23}
b = {"city": "Bhopal", "course": "Python"}
a.update(b)
print(a)'''


# Q19. Dictionary reverse 
'''a = {
    "a": 1,
    "b": 2,
    "c": 3
}
d = {}
for key,value in a.items():
    d[value] = key
print(d)    '''

# Q21. Highest frequency character
'''a = "mississippi"

highest = 0
for i in a:
    if a.count(i) > highest:
        highest = a.count(i)
print(highest,i)        
'''

# Q22. Highest frequency word
'''a = ["python", "java", "python", "django", "python", "java"]
heighest = 0
for i in a:
    if a.count(i) > heighest:
        heighest = a.count(i)
        res = i
print(heighest,res)    '''    

# Q23. Second highest value 
'''
marks = {
    "A": 50,
    "B": 90,
    "C": 70,
    "D": 80
}
list = []
for key,value in marks.items():
    list.append(value)
highest = 0
second_high = 0
for i in list:
    if i > highest:
        second_high = highest
        highest = i
    elif i > second_high:
        second_high = i
for key,value in marks.items():
    if value == second_high:
        res = key        
print(key,":",second_high)  '''  

# l = ["now","cow","boy","book","nice","hi","by","i"] 

# for i in range(len(l)):
#     # if len(l[i]) == 1:
#     #     d[1] = l[i]   
#     # elif len(l[i]) == 2:
#     #     d[2] = l[i]   
#     if len(l[i]) == 3:
#         d[3] = list(l[i])            
               
# print(d)       
    # if l[i] == :
    #     print(l[i])

# l = ["now","cow","boy","book","nice","hi","by","i"]    
# finalD = {}
# d1 = []
# d2 =[]
# d3 = []
# d4 = []
# for i in range(len(l)):
#     if len(l[i]) == 4:
#         d1.append(l[i]) 
#     elif len(l[i]) == 3:
#         d2.append(l[i])  
#     elif len(l[i]) == 2:
#         d3.append(l[i])
#     elif len(l[i]) == 1:
#         d4.append(l[i])     
# finalD.update({4:d1,3:d2,2:d3,1:d4})
# print(finalD)

# l = ["now","cow","boy","book","nice","hi","by","i"]    
# finalD = {}
# for i in l:
#     length = len(i)

# l = [4,3,2,2,3,2,3,1,2,1]
'''rev = []
for i in range(len(l)):
    x = (len(l)- 1) - i
    rev.append(l[x])
building = 0
for i in rev:
    if i  >= building:
        print(i)
        building = i'''







              
# print(empty_list)
      
