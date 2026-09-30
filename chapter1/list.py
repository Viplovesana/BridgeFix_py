'''fruits = ["apple","bannana","mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])'''

# list[start:stop:step]

'''numbers = [10, 20, 30, 40, 50]
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)'''
'''print(numbers[1:4])
print(numbers[2:4])
print(numbers[0:2])
'''
# reverse of list 
'''numbers = [10, 20, 30, 40, 50]
print(numbers[::-1])
'''

# numbers = [10, 20, 30, 40, 50]
# print(len(numbers))
# numbers.append(60)
# print(numbers)
# numbers.append([60,70,80])
# print(numbers)
'''numbers.extend([60,70,80])
print(numbers)'''
'''numbers.insert(4,45)
print(numbers)
numbers.remove(50)
print(numbers)'''
'''numbers = [10, 20, 30, 40, 50]
x = numbers.pop(1)
print(x)
print(numbers)'''

'''numbers = [10, 20, 30, 40, 50]
numbers.clear()
print(numbers)'''

'''numbers = [10, 20, 30, 40, 50]
print(numbers.index(20))'''

'''numbers = [10, 20, 30,20, 40, 50]
print(numbers.count(20))'''

'''numbers = [50, 30, 10, 20]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)'''

'''a = [1,2,3,4]
b = a
b.append(100)
print(b) '''  
import copy
# SHALLOW COPY------------
# a = [[10,20],[30,40]]
# b = copy.copy(a)
# print(b)
# print(a)
# b[0].append(100)
# print(b)
# print(a)
# b.append([50,60])
# print(b)
# print(a)

# DEEP COPY--------

'''a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(100)
print(b)
print(a)
b.append([5,6])
print(b)
print(a)'''

# a = [1,2] 
# b = [3,4]
# c = a + b 
# print(c)

# x = [1,2]
# print(x*3)

'''fruits = ["apple","banana","mango"]
for index,value in enumerate(fruits):# enumerate gives the position of element
    print(index,value)'''

'''n = [1,2,3,4]# list unpacking-------
a,b,c,d = n
print(c)'''

'''n = [10,20,30,40]
a,*b = n
print(b)'''

'''x = [10,20,30,40]
x.reverse()
print(x)'''

# -----------questions-----------------------------------------------

# 1. Sum of all elements
'''a = [10, 20, 30, 40, 50]

sum = 0
for i in a:
    sum = sum + i
print(sum)'''

# 2. Find largest number

# a = [10, 45, 23, 89, 12]

# largest = 0
# for i in a:
#     if i > largest:
#         largest = i
# print(largest)        
'''
students = ["Ajay","Ravi","Neha"]
scores = [85,90,88]

student_record = {"school":"DPS Indore"}
records = []
for key,value in enumerate(students):
    student_record["score"] = scores[key]
    student_record["name"] = students[key]

    # print(student_record)
    records.append(student_record)

print(records)    
'''

# 3. Find smallest number
'''a = [100,10, 45, 23, 89, 12]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)        '''

# 4. Count even and odd numbers
'''a = [1, 2, 3, 4, 5, 6, 7]

even = 0
odd = 0 
for i in a:
    if i % 2==0:
        even+=1
    else:
        odd+=1
print(even)            
print(odd)            
'''

# 5. Reverse a list
'''a = [1, 2, 3, 4, 5]

n = len(a)
print(n)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)            
'''
# 6. rmove duplicate elements

'''a = [1, 2, 3, 2, 4, 5, 1, 6]    
new = []
for i in set(a):
    if a.count(i) > 1:
       continue
    new.append(i)
print(new)'''


# 6. Find duplicate elements

# a = [1, 2, 3, 2, 4, 5, 1, 6]    
# new = []
# for i in set(a):
#     if a.count(i) > 1:
#         new.append(i)
# print(new)

'''# 9. Find second largest number 
a = [10, 50, 20, 80, 30]

sec_large = 0 
for i in a:
    if i > sec_large:
        sec_large = i
        res = sec_large
print(res)        
'''


'''a = [10, 50, 20, 80, 30]

large = 0
sec_large = 0

for i in a:
    if i > large:
        sec_large = large
        large = i
    elif i > sec_large:
        sec_large = i
      
print(sec_large)   '''    

# 23. Check whether list is palindrome
'''a = [1, 2, 3, 2, 1]
empty = []
for i in range(len(a)):
    b = (len(a) - 1) - i
    empty.append(a[b])  
if a == empty:
    print("palindrom") 
else:
    print("not palindrom")     '''   

# Q1. List me consecutive duplicate elements hatao:

# a = [1, 1, 2, 2, 2, 3, 1, 1, 4]

# for i in range(len(a)):
    
# Q3.List ko left side se 1 position rotate karo, bina pop()/insert() ke:

'''a = [1, 2, 3, 4, 5]    
b = len(a)
for i in range(b-1):
    for j in range(b-i-1):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    break
print(a)  '''      

# Q5.List me aise elements nikalo jo apne index ke equal hain:

'''a = [0, 5, 2, 7, 4, 10]
for i in a:
    if i == a.index(i):
        print(i)'''

# Q2. List me largest aur smallest number ke beech ka difference nikalo:

'''a = [10, 45, 2, 89, 23, 7]
smallest = a[0]
largest = 0
for i in a:
    if i < smallest:
        smallest = i
print(smallest)
for i in a:
    if i > largest:
        largest = i
print(largest)
a = smallest
b = largest 
print(b-a)
'''
'''a = [1,1,2,3,4,4,4,5,2]
current = 0
maximum = 0
previous = 0
for i in a:
    if a.count(i) > maximum:
        maximum = a.count(i)
print(maximum,i)'''
       
    # if a.count(i) > largest:
    #     largest = a.count(i)
    #     print(largest,i)


'''def recursive(nested):
    flaten = []
    for i in nested:
        if isinstance(i,list):
            flaten.extend(recursive(i))
        else:
            flaten.append(i)
    return(flaten)            
l = [[1,2,[10,12],0,],[[13,14,15,[7,77,[90,50]]],3,4],[5,6]]   
res = recursive(l)
print(res)
'''
'''l = [4,3,2,2,3,2,3,1,2,1]
new_list = []
for i in range(len(l)):
    x = (len(l) - 1)-i
    new_list.append(l[x])
building = 0
for i in new_list:
    if i >= building:
        # print(i)
        building = i    
        print(building)        
     '''





# l = [1,3,4,6,5,9,8]

# def func(x):
#     return x%2!=0
# r =filter(func,l)
# print(list(r))


# def func(x):
#     return x%2!=0
# print(func(1))
#print(list(r))


def recursive(listing):
    flaten = [] 
    for i in listing:
        if isinstance(i,list):
            flaten.extend(recursive(i))
        else:
            flaten.append(i)
    return(flaten)
l = [[1,2,[10,12],0,],[[13,14,15,[7,77,[90,50]]],3,4],[5,6]]   
res = recursive(l)
print(res)
