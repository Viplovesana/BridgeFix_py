# MAP =============================================================================================
# Q1. Har number ka square nikalo
'''a = [1, 2, 3, 4, 5]
def func(ans):
    return ans * ans
res = map(func,a)
print(list(res))'''

# Q2. Har number ko double karo
'''a = [2, 4, 6, 8]
def func(ans):
    return ans + ans
res = map(func,a)
print(list(res))
'''

# Q4. Strings ko uppercase karo and len
# '''a = ["python", "django", "sql"]
# def func(ans):
#     return len(ans)
# res = map(func,a)
# print(list(res))'''

# Q6. Numbers ko even/odd me convert karo
'''a = [1, 2, 3, 4, 5, 6]
def func(b):
    if b %2==0:
        return "even"
    else:
        return "odd"
res = map(func,a)
print(list(res))   ''' 

# Q7. Positive/Negative/Zero
'''a = [-5, 3, 0, -2, 8]
def func(b):
    if b > 0:
        return "positive"
    elif b<0:
        return "negative"
    else:
        return "Zero"
res = map(func,a)
print(list(res)) 
    '''

# Q8. Names ko "Hello " ke saath combine karo
'''names = ["Viplove", "Rahul", "Aman"]

a = [-5, 3, 0, -2, 8]
def func(b):
    return b + " hello"
res = map(func,names)
print(list(res)) '''

# Q9. Celsius → Fahrenheit

# Formula:

# 
'''c = [0, 10, 20, 30]
def func(b):
    return b * 9/5 + 32
res = map(func,c)
print(list(res)) '''

# Q10. Strings ko integers me convert karo
'''a = ["10", "20", "30", "40"]
def func(b):
    return int(b)
res = map(func,a)
print(list(res)) '''

# Q11. Do lists ke corresponding elements add karo
'''a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

def func(a,b):
    return a+b
res = map(func,a,b)
print(list(res)) '''

# Q13. Do strings ke corresponding characters combine karo
'''a = ["A", "B", "C"]
b = ["1", "2", "3"]

def func(a,b):
    return a+b
res = map(func,a,b)
print(list(res))'''


'''a = ["cat", "python", "hi", "developer"]
def func(a):
    return len(a)
res = map(func,a)
print(list(res))'''

# Q18. Names ki first letter nikalo
'''names = ["Viplove", "Rahul", "Aman", "Rohit"]
def func(a):
    return a[0]
res = map(func,names)
print(list(res))
'''

# Q19. List ke numbers ko string me convert karo
'''a = [10, 20, 30, 40]
def func(a):
    return str(a)
res = map(func,a)
print(list(res))
'''

'''students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 35},
    {"name": "C", "marks": 65}
]
def func(students):
        x = students["marks"]  
        if x > 40:
                return "pass"
        else:
                return "fail"  

res = map(func,students)
print(list(res))'''

# Q28. Numbers ko absolute value me convert karo
'''a = [-10, -5, 0, 5, 10]
def func(a):
    return abs(a)
res = map(func,a)
print(list(res))'''


# Q26. Har sentence ko words ki list me convert karo
'''a = [
    "I love Python",
    "Django is easy",
    "Python is powerful"
]
def func(a):
    return a.split()
res = map(func,a)
print(list(res))
'''

# Q25. map() se strings ke spaces remove karo
'''a = ["hello world", "python developer", "django developer"]

def func(a):
    return a.replace(" ","")
res = map(func,a)
print(list(res))
'''

# Q24. Nested list ke har element ko double karo
'''a = [
    [1, 2],
    [3, 4],
    [5, 6]
]
def func(a):
    return a
res = map(func,a)
print(list(res))'''

'''# Q22. Two lists se dictionary banao using map()
keys = ["name", "age", "city"]
values = ["Viplove", 23, "Bhopal"]

def func(keys,values):
    x = keys,values
    return x
res = map(func,keys,values)
print(dict(res))

'''
#  Q21. Names ko length ke saath pair karo
'''names = ["Viplove", "Aman", "Rahul"]  
def func(a):
    return a,len(a)
res = map(func,names)
print(list(res))'''


# FILTER ======================================================================================


#  Q1. Sirf even numbers nikalo
'''a = [1, 2, 3, 4, 5, 6]   

def even(x):
    if x%2==0:
        return x
res = filter(even,a)
print(list(res))
'''

# Q6. Sirf even-length words
'''a = ["cat", "python", "hi", "django", "sql"]
def even(x):
    if len(x) % 2==0:
        return x
res = filter(even,a)
print(list(res))'''


# Q8. Sirf uppercase strings
'''a = ["PYTHON", "Django", "SQL", "React", "API"]
def even(x):
    if x.isupper():
        return x
res = filter(even,a)
print(list(res))'''


# # 9. Sirf vowels se start hone wale words
# a = ["apple", "banana", "orange", "grapes", "umbr"]
# def even(x):
#     if x[0] in "aeiou":
#         return x
# res = filter(even,a)
# print(list(res))



# Q24. Duplicate numbers me se sirf numbers jo repeat hue hain
# 
'''a = [1, 2, 3, 2, 4, 5, 1, 6, 3]
def duplicate(x):
    if a.count(x)>1:
        return x
res = filter(duplicate,a)
print(list(set(res)))'''

# Q19. Employees filter
'''
employees = [
    {"name": "A", "salary": 45000, "age": 22},
    {"name": "B", "salary": 70000, "age": 25},
    {"name": "C", "salary": 80000, "age": 30},
    {"name": "D", "salary": 35000, "age": 21}
]

def func(emp):
    if emp["salary"] > 60000 and emp["age"] < 30:
        return emp
res = filter(func,employees)
print(list(res))'''

# Q18. String + condition
'''
l = ["apple", "cat", "application", "dog", "avocado", "python"]

def func(b):
    if b[0] == "a" and len(b) <= 5:
        return b
res = filter(func,l)
print(list(res))
'''

# Q12. Salary > 50000

'''employees = {
    "A": 45000,
    "B": 70000,
    "C": 35000,
    "D": 90000
}
def func(b):
    if employees[b] > 50000:
        return (b,employees[b])
res = filter(func,employees)
print(list(res))
 '''

# REDUCE=============================================================================================

from functools import reduce

'''l1 = [1,2,3,4,5]
def add(x,y):
    return x+y
res = reduce(add,l1)
print(res)
'''

# Q3. Find maximum
'''
a = [10, 25, 7, 45, 18]
def max(x,y):
    if x>y:
        return x
    else:
        return y 
res = reduce(max,a)
print(res)'''

# Q5. Concatenate strings

'''a = ["Python", "Django", "DRF"]
def func(a,b):
    return a+b
res = reduce(func,a)
print(res)
'''

'''a = [1, 2, 3, 4, 5, 6, 7, 8]

def func(x,y):
    if y%2==0:
       return x+y
    else:
       return x
res = reduce(func,a)
print(res)'''

# Q7. Sum of odd numbers

'''a = [1, 2, 3, 4, 5, 6, 7, 8]
def func(x,y):
    if y%2!=0:
        return x+y
    else:
        return x
r = reduce(func,a,0)
print(r)  '''  
'''
a = ["cat", "elephant", "dog", "tiger"]
def func(x,y):
    if len(x)<len(y) :
        return x
    else:
        return y
r = reduce(func,a)
print(r) 
'''

# Q11. Find second largest number

'''a = [10, 50, 20, 80, 30, 70]
def func(x,y):
    if x>y :
        return x
    else: 
        return y
r = reduce(func,a)
print(r) '''
'''
# Q11. Find second largest number         

a = [10, 50, 20, 80, 30, 70]

def func(x,y):
    if x > y:
        return y
    else:
        return y
r = reduce(func,a)
print(r)    '''

# ===================== LAMDA FUNCTION ============================================================

# normal function ---
'''def square(x):
    return x*x
print(square(2))'''

# recursive----

# square = lambda x : x*x
# print(square(2))     
# Q2. Lambda function banao jo number ka cube return kare.
'''square = lambda x:x**3
print(square(2))'''

# 3. Lambda function banao jo number ko 10 se add kare.
'''add = lambda x : x + 10
print(add(5))'''

# Q4. Do numbers ka addition lambda se karo.

# 10, 20 → 30
'''
add = lambda a,b: a+b 
print(add(12,59))'''

'''Q5. Do numbers ka multiplication lambda se karo.

5, 6 → 30'''

'''multiple = lambda a,b : a * b
print(multiple(2,8))'''


# multiplication by lamda 

# multi  = lambda x: x*5
# print(multi(6))

'''find = lambda x : "big" if x>10 else "small"
print(find(20))'''

# a = [1,2,3,4,5,6,8,34,98]

'''result = map(lambda x: x*2,a)
print(list(result))'''

# greater number-----
'''
res = filter(lambda x:x>6,a)
print(list(res))'''

'''from functools import reduce
a = [10,20,30,40,50,60]
result = reduce(lambda x,y: x+y ,a)
print(result)
'''

# 8. List me kitne elements hain?
'''a = [10, 20, 30, 40, 50]

result = map(lambda x : 1 ,a)
print(sum(result))'''

# Q12. Strings ko uppercase karo
'''a = ["python", "django", "lambda"]

result = map(lambda x : x.upper(),a)
print(list(result))'''

# Q13. Sirf even numbers
'''a = [1, 2, 3, 4, 5, 6, 7, 8]

res = filter(lambda x: x%2==0 ,a)
print(list(res))'''


# Q16. Sirf words jinki length > 5
'''a = ["apple", "banana", "cat", "python", "dog", "django"]

res = filter(lambda x : len(x)>5 ,a)
print(list(res))'''

# Q18. Product
'''from functools import reduce
a = [2, 3, 4, 5]

res = reduce(lambda x,y : x*y,a)
print(res)'''

# Q19. Maximum using reduce
'''from functools import reduce
a = [10, 50, 30, 90, 20]

res = reduce(lambda x,y:x if x>y else y ,a)
print(res)'''


# Step 1: filter() se even numbers nikalo.

# Step 2: map() se unka square karo.
'''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res1  = filter(lambda x: x%2==0,a)
res2  =map(lambda y:y*y,res1)
print(list(res2)) 
                    '''


# Sirf even numbers lo aur unka sum nikalo.
'''from functools import reduce
a = [1, 2, 3, 4, 5, 6]
res1 = filter(lambda x: x%2==0,a)
res2 = reduce(lambda x,y: x+y,res1)
print(res2)
   '''

# Q3. Numbers greater than 50 → square → sum
'''from functools import reduce
a = [10, 60, 20, 70, 30, 80]
greater = filter(lambda x: x>50,a)
square = map(lambda y: y*y ,greater)
sum = reduce(lambda a,b:a+b,square)
print(sum)
'''

# Q4. Maximum using reduce()
# from functools import reduce
'''a = [45, 12, 89, 34, 67, 99, 23]
maximum = reduce(lambda x,y:x if x>y else y,a)
print(maximum)
'''
# Q5. Minimum using reduce()
'''from functools import reduce
a = [45, 12, 89, 34, 67, 99, 23]
minimum = reduce(lambda x,y:x if x<y else y,a)
print(minimum)'''

# Q6. Words ki length
'''words = ["python", "django", "api", "lambda", "backend"]
length = map(lambda x: len(x),words)
print(list(length))  '''

# Q7. Long words filter karo
'''words = ["cat", "python", "dog", "developer", "api", "django"]
long = filter(lambda x,y : len(x)>len(y),words)'''

# 8. Longest word using reduce
from functools import reduce
'''words = ["cat", "python", "developer", "api", "django"]
res = reduce(lambda x,y: x if len(x)>len(y) else y,words)
print(res)'''

'''employees = {
    "A": 45000,
    "B": 70000,
    "C": 35000,
    "D": 90000,
    "E": 60000
}     
res = filter(lambda x : employees[x]>50000, employees)
result = {i : employees[i] for i in res}
print(result)'''


# # Q11. Salary ke basis par sort
# employees = {
#     "A": 45000,
#     "B": 70000,
#     "C": 35000,
#     "D": 90000
# }

# res = sorted(employees.items())
# print(res)

# Q13. Second highest salary
# Lambda + sorted() use karo.

'''employees = {
    "A": 45000,
    "B": 70000,
    "C": 35000,
    "D": 90000,
    "E": 80000
}
largest = 0
second_largwst = 0
for key ,value in employees.items():
    if value > largest:
        second_largwst = largest
        largest = value
    elif value > second_largwst:
        second_largwst = value
print(second_largwst)          
print(largest)  ''' 

'''employees = {
    "A": 45000,
    "B": 70000,
    "C": 35000,
    "D": 90000,
    "E": 80000
}

res = sorted(employees.items(), key=lambda x: x[1], reverse=True)

print(res[1])'''



# Lambda ke concept ka use karke duplicate values identify/process karo.

'''a = [1, 2, 3, 2, 4, 5, 1, 6, 3]

ress = list(set(a))
print(ress)

res = filter(lambda x : a.count(x)>1 ,a)
print(list(set(res)))'''


