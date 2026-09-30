# 1. Numbers ko squares mein convert karo
'''a = [1, 2, 3, 4, 5]
x = {i:i*i for i in a }
print(x)'''

'''a = [1, 2, 3, 4, 5]
x = {i:i**3 for i in a }
print(x)'''                                   

# 4. List ko dictionary mein convert karo
'''a = ["python", "django", "react"]
x = {i : len(i) for i in a }
print(x)'''

# Q5. Numbers ka square sirf even numbers ke liye
'''x = {i :i*i for i in range(1, 11) if i%2==0}
print(x)

x = {i :i*i for i in range(1, 11) if i%2!=0}
print(x)'''

# Q9. Even/Odd dictionary
'''a = [1, 2, 3, 4, 5]
x = {i:"even" if i%2==0  else "odd"  for i in a  }
print(x)
'''

# Q2. Positive/Negative
'''a = [-5, 2, -3, 8, 0, -1]
x = {i:"positive" if i>0 else "negative" for i in a}
print(x)'''

# Q3. Pass/Fail
'''marks = {
    "math": 80,
    "science": 35,
    "english": 67,
    "hindi": 28
}
x = {key:"pass" if value > 40 else "fail" for key,value in marks.items()}
print(x)
'''

# Q4. Number aur uska square/cube

# Agar number even hai → square
# Agar odd hai → cube

'''a = [1, 2, 3, 4, 5]
x = {i:i*i if i%2==0 else i**3 for i in a}
print(x)'''

# Level 2 — Thoda logic
# Q5. Adult/Minor
'''ages = {
    "A": 17,
    "B": 25,
    "C": 15,
    "D": 32
}
x={key:"major" if value >= 18 else "minor" for key,value in ages.items()}
print(x)'''

# Q6. Divisible by 3
# a = [3, 5, 9, 10, 12, 14]
# {
#     3: "yes",
#     5: "no",
#     9: "yes",
#     10: "no",
#     12: "yes",
#     14: "no"
# }
# x={i:"yes" if i%3==0 else "no" for i in a}
# print(x)

'''a = [1, 2, 3, 4, 5]
result = {}
for i in a:
    if i % 2 == 0:
        result[i] = i * 2
    else:
        result[i] = i * 3
print(result)

x = {i:i*2 if i%2==0 else i*3 for i in a}
print(x)'''

# Q15. Nested condition 
'''marks = {
    "Python": 85,
    "Django": 72,
    "SQL": 38,
    "React": 25
    
}
x={key:"Exelent" if value >=80 
   else "good" if value >=60 
   else "pass" if value >=33 
   else "fail" 
   for key,value in marks.items()}
print(x)'''


# a = [1,3,5,7,9]
# b = [2,4,6,8,10]
# empty = {}
# for i in range(len(a)):
#     empty[a[i]] = b[i]
# print(empty)

'''a = [1,3,5,7,9]
b = [2,4,6,8,10]'''
'''res = {a[i]:b[i] for i in range(len(a))}
print(res)'''
'''empty = dict(zip(a,b))
print(empty)'''

# l = [1,0,1,0,1,0,1,0,1,0,1]
# count0 = 0    
# count1 = 0    
# i = 0
# while i < len(l):
#     count1+=(l[i]==1)
#     count0+=(l[i]==0)
#     i+=1
# print(count1)
# print(count0)

# l = [1,0,1,0,1,0,1,0,1,0,1]
# x = sum(l)
# print(x)
# y = len(l)
# print(y-x)



  
