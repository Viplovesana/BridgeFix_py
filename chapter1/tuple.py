# Q1. Tuple banao aur print karo:

'''a = (10, 20, 30, 40, 50)
print(a[::4])'''

# Q6. Tuple ke saare numbers ka sum find karo without sum().

'''a = (10, 20, 30, 40)

sum = 0
for i in a:
    sum = i + sum
print(sum)'''

# # Q7. Tuple mein maximum number find karo without max().

# a = (10, 50, 20, 80, 30)

# max_no = 0
# for i in a:
#     if i > max_no:
#         max_no = i 
# print(max_no)

# Q7. Tuple mein minimum number find karo without max().

'''a = (10, 50, 20, 80, 30)

min_no = a[0]
for i in a:
    if i < min_no:
        max_no = i 
print(min_no)'''

# Q9. Tuple mein even aur odd numbers count karo.

'''a = (10, 13, 22, 35, 40, 51)
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
print(tuple(even))
for i in a:
    if i % 2!= 0:
        odd.append(i)
print(tuple(odd))  '''  

# Q10. Tuple mein kisi particular number ki frequency find karo without count().

'''a = (1, 2, 2, 3, 2, 4, 2)
frequency = 0
for i in a:
    if a.count(i) > 1:
        frequency+=1
print(frequency,i)'''

# Q11. Tuple ko reverse karo without [::-1] aur reversed().

'''a = (1, 2, 3, 4, 5)
rev = []
for i in range(len(a)):
    x = (len(a)-1) - i

    rev.append(a[x])    
print(tuple(rev))    
'''

# Sirf woh elements print karo jo exactly ek baar aaye hain.
'''
a = (1, 2, 2, 3, 4, 4, 5, 6, 6)
new = []
for i in a:
    if a.count(i) == 1:
        new.append(i)
print(tuple(new))'''    

#-------------------- CONSICUTIVE ELEMENT-----------------------

'''a = (1, 1, 2, 3, 4, 4, 4, 5, 2, 1)
consigutive = []
x=a[0]
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        if a[i] > x:
            consigutive.append(a[i])
print(set(consigutive))
'''

# Q21. Nested Tuple

'''a = ((1, 2), (3, 4), (5, 6))
new_list = []
for i in range(len(a)):
    for j in a[i]:   
        new_list.append(j)
print(tuple(new_list))'''

# Q22. Nested tuple ka sum

'''a = ((1, 2), (3, 4), (5, 6))
# a = list(a)
# print(a)
total = 0
for i in range(len(a)):
    print(a[i])
    for j in range(len(a)-i-1):
        total = total + j
        
print(total) '''
       
    
    # print(a[i])
         
# print(sum)    

# Q23. Tuple ke andar tuple
a = (10, (20, 30), 40, (50, 60))
b = []
for i in a:
    if type(i) == tuple:
        b.append(i)
        break
y = []        
for x in b:
    y.append(x)
# print(y)  


# for i in a:
#     if 



'''a = (10, (20, 30), 40, (50, 60))    

for i in range(len(a)):'''
    #   print(a[i])

    # for j in range(len(a))


        
       