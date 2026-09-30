
# ================================GENERATOR===============================================================

'''def count(n):
    i = 1 
    while i <=n:
        yield i
        i+=1
res = count(5)        
for i in res:
    print(i)'''

# =======================================

'''def generate():
    print("A")
    yield 10
    print("B")  
    yield 20
    print("C")
    yield 30

res = generate()
print(next(res))
# print(next(res))
# print(next(res))'''

# =========================================

'''def genrate(n):
    # i = 1
    # while i <=n:
    #     yield i
    #     i+=1
    for i in range(1,n+1):
        yield i
    # yield 11
    # yield 12
    # yield 13
    # yield 14
for gen in genrate(10):
    print(gen) '''   

# ========================================

'''def genrate(data):
    for i in data:
        yield i
for gen in genrate([11,22,33,44,55]):
    print(gen)       
'''

'''def genrate(data):
    for i in data:
        yield i
for gen in genrate("PYTHON"):
    print(gen) '''

# GENRATOR EXPRESSION =========================================> 

'''def func(n):
    for i in range(1,n+1):
        yield i * i       # normal function genrator === >> 
res = func(10)
print(next(res))        
print(next(res))        
print(next(res))  '''      

# result = (x * x for x in range(1,11))
# print(type(result))
# print(next(result))
# print(next(result))


'''result = (x * x for x in range(1,11))
for gen in result:
    print(gen)'''

# Q1 — Even numbers
# Generator banao jo 1 se 20 tak sirf even numbers de.
'''
def func():
    for i in range(1,21):
        if i %2==0:
            yield i 
for gen in func():
    print(gen)       '''    

'''
res = (x for x in range(1,21) if x%2==0)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
'''
# Q4 — String characters
# characters("PYTHON")
'''
square = (i for i in "PYTHON")
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
print(next(square))
'''

# def generate():
#     print("hi")
#     yield 10 
#     print("viplove")
#     yield 20
#     print("how are you")
#     yield 30
# res = generate()
# a = next(res)
# print(a)
# b = next(res)
# print(b)
# c = print(next(res))
   

# 🟢 Now Hard — Question 1

# Given:

# numbers = range(1, 31)

# Create one generator expression with these rules:

# Even and divisible by 4 → square
# Odd and divisible by 3 → cube
# Ignore all other numbers

# Then print all generated values using a for loop.

# Send your code.   


'''res = (i*i if i%2==0 and i%4==0 else i**3 for i in range(1,31) if i%3==0 )
for i in res:
    print(i)
'''

