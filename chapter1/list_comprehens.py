
# x = []
# for i in range(1,6):
#     x.append(i)
# print(x)   
# x = [i for i in range(1,6)]
# print(x)

# Q2. Numbers ka square
'''a = [1, 2, 3, 4, 5]
x = [i*i for i in a]
print(x)'''

'''a = [2, 4, 6, 8]
x = [i*2 for i in a]
print(x)'''

'''a = "python"
# Output:
# ['p', 'y', 't', 'h', 'o', 'n']
x = [i for i in a.upper()]
print(" ".join(x))'''

# Q7. 1–10 ke cubes banao.
'''
x = [i**3 for i in range(1,11)]
print(x)'''

# Q8. 1–20 ke even numbers nikalo.
'''x = [i for i in range(1,21) if i%2==0]
print(x)'''

# x = [i for i in range(1,21) if i%2!=0]
# print(x)

# x = [i+10 for i in range(1,6)]
# print(x)

# Q11. Sirf positive numbers
'''a = [-5, 2, -8, 10, -3, 7]
x = [i for i in a if i>0]
print(x)'''

# a = [-5, 2, -8, 10, -3, 7]
# x = [i for i in a if i<0]
# print(x)

# Q14. Sirf numbers divisible by 5.

'''x = [i for i in a if i%5==0]
print(x)
'''
# Q15. Sirf numbers divisible by both 2 and 3.
'''a = [2, 3, 4, 6, 8, 9, 12, 15, 18]
x = [i for i in a if i%2==0 and i%3==0]
print(x)'''

# Q16. List mein se 5 se chhote numbers nikalo.
# a = [2, 3, 4, 6, 8, 9, 12, 15, 18]
'''x = [i for i in a if i < 5 ]
print(x)'''

# Q17. Sirf even numbers ka square nikalo.

'''x = [i*2 for i in a if i%2==0 ]
print(x)'''

# Q18. Sirf odd numbers ka cube nikalo.
# a = [2, 3, 4, 6, 8, 9, 12, 15, 18]
# x = [i**3 for i in a if i%2!=0 ]
# print(x)

# Q19. Sirf numbers jo 10 aur 50 ke beech hain.
# a = [2, 3, 4, 6, 8, 9, 12, 15, 18,21,43]
# x = [i for i in a if i>10 and i<20]
# print(x)
'''a = [0, 2, 0, 5, 7, 0, 3]
x = [i for i in a if i>0]
print(x)
'''

# Q21. Sirf vowels nikalo
'''a = "pythonprogramming" 
x = [i for i in a if i in "aeiou"]
print(x)'''
# only consonant----------------------
'''x = [i for i in a if i not in "aeiou"]
print(x)'''

# Q23. String mein spaces remove karo.
'''a = "hello world python"
x = [i for i in a if i not in " "]
print("".join(x))'''

# Q24. Sirf uppercase characters nikalo.
'''a = "PyThOn"
x = [i for i in a if i.isupper() ]
print(x)'''

# a = "pythonprogramming" 
'''x = [i for i in a if a.count(i) > 1]
print(x)'''
'''max_count = 0
x = [max_count for i in a if a.count(i) > max_count max_count = a.count(i)]
print(max_count)'''

# Q8 — Sirf duplicate numbers nikalo.

'''a = [1, 2, 2, 3, 4, 4, 5, 5, 5]
x = [i for i in a if a.count(i) > 1]
print(x)'''

# Q9 — Frequency
# a = [1, 2, 2, 3, 4, 4, 5, 5, 5]
'''y = {}
for i in a:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1
print(y)     
'''
'''x = {i:a.count(i) for i in a}
print(x)
'''

# l = [[1,2,[10,12],0,],[[13,14,15,[7,77,[90,50]]],3,4],[5,6]] 
# l2 = []
# x = [i for i in l if isinstance(i,list)]
# print(x)


'''c  = ["same" if a.count(i) == b.count(i) else "not same" for i in a ]
print(c)'''

'''l = [1,2,3,4,5,6,7,8,9]
new = [i*i if i%2==0 else i**3 for i in l if i > 3]
print(new)'''

'''l = [1,2,3,4,5,6,7,8,9]
new = [i*i for i in l  if i%4==0 ]
print(new)

l = [1,2,3,4,5,6,7,8,9]
new = [i**i for i in l  if i%3==0 ]
print(new)
'''
'''l = [1,2,3,4,5,6,7,8,9,10,11,12]
new = [i*i if i%4==0 else i**3 for i in l if i%3==0 or i%4==0]
print(new)'''


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Using one list comprehension:

# If the number is even and divisible by 4 → calculate its square
# If the number is odd and divisible by 3 → calculate its cube
# If the number is greater than 15 and divisible by 5 → calculate its double
# Ignore all other numbers.

# Write only one list comprehension.

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# result = [x*x if x % 4 == 0 else x**3 if x % 3 == 0 else x*2
#           for x in numbers if (x % 2 == 0 and x % 4 == 0) or (x % 2 != 0 and x % 3 == 0) or (x > 15 and x % 5 == 0)]
# print(result)


# If the number is even and divisible by 4 → calculate its square
# If the number is odd and divisible by 3 → calculate its cube
# If the number is greater than 15 and divisible by 5 → calculate its double
# Ignore all other numbers.
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17,18,19,20]

# new = [i*i if i%4==0 else i**3 for i in num if (i%3==0 or i%4==0) if (i>15 and i%5==0) else]
# print(new)

