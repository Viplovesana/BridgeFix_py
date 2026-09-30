# s = "python"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[-1])
# print(s[-2])
# print(s[-3])
# s = "python"
# string[start:stop:step]

'''print(s[0:4])
print(s[::2])
print(s[::-1])'''

# s = "python"

'''s[0] = "j"# it will not changed bcs it is immutable
print(s)'''

'''s = "j" + s[1:]
print(s)
s = "python"
s = "s" + s[2:]
print(s)
s = "j" + s[1:]
print(s)
'''
# s = "python"

# s = s[:2] + "x" + s[3:]
# print(s)

# string repetation------

# print(s*3)

# Membership operator--------

# s = "python programming"

'''print("python" in s)
print("java" not in s)'''

# s = "python"
# print(len(s))

s = "python"

# s2 = "ythonOn"
# print(s.upper())
# print(s2.lower())
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())
# print(s.count("o"))
'''print(s.find("y"))
print(s.find("z"))
print(s.index("y"))# return -1
print(s.index("z")) # valueeeror'''
# print(s.endswith("on"))
# print(s.endswith("is"))
# s = "i know python"
# print(s.replace("know","love"))
# print(s.split())# it will split intop a string
# s = "i,know,python"
# print(s.split(","))
'''s = ["pyhton","is","easy"]
print(" ".join(s))'''

'''s = ["a","b","c"]
print("-".join(s))'''

'''s = " python "
print(s.strip())
s = " python"
print(s.lstrip())
s = "python "
print(s.rstrip())'''

'''s = "python"
print(s.center(10))
print(s.ljust(15,"-"))
print(s.rjust(15,"-"))'''

'''num = "25"
print(num.zfill(6))'''

'''s = "Python"
print(s.isalpha())
print(s.isdigit())
print(s.isdecimal())
print(s.isnumeric())
print(s.isspace())
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.isidentifier())
print(s.isprintable())
print(s.isascii())
print(s.isascii())'''

# s = "python programming"
# print(s.removeprefix("python "))
# print(s.removesuffix(" programming"))

# s = "python"
# print(s.encode())

# s = "python\tdeveloper"
# print(s.expandtabs(10))

# s = "hello\npython\nworld"
# print(s.splitlines())

# s = "python"
# rev = ""
# for i in s:
#     rev = i + rev
# print(rev)    


'''s = "programming"

for i in s.upper():
    if i in "AEIOU":
        print(i)'''

'''s = "banana"
empty = {}
for i in s:
    if i in empty:
        empty[i] += 1
    else:
        empty[i] = 1 
print(empty)  '''          


# print(s.count("a"))
# s = "banana"
# count = 0 
# for i in s:
#     if i is "a":
#         count = count +1
# print( f"{s} is a {count} count")


# 4. First and last character

'''s = "developer"

# print(s[::8])
for i in range(len(s)):
    if i == 0 or i == len(s)-1:
        print(s[i])'''

'''# 5. Remove spaces

s = "p y t h o n"
for i in s:
    if i == " ":
        continue
    print(i)'''

'''s = "p y t h o n"
new_string = " "
for i in s:
    if i == " ":
        continue
    new_string = new_string + i
print(new_string.lstrip())'''

# 8. Find duplicate characters

'''s = "programming"

for i in set(s):
    if s.count(i) > 1:
         print(i)
'''
'''a = "accdea"
order = ""

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if ord(a[i]) > ord(a[j]):
            a = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]

print(a)
# 9. Remov'''
# e duplicate characters

'''s = "programming"
new_string = " "
for i in s:
    if s.count(i) == 1:
        new_string = new_string + i
print(new_string) ''' 

# 10. Find the longest word

'''s = "Python is very powerful language"
greater = 0

for i in s.split():
    if  len(i) > greater:
        greater = len(i)
print(i)'''

'''# 12. Reverse each word

s = "Python is easy"
rev = " "
for i in s.split():
    rev = rev + i[::-1] + " "
print(rev.lstrip())
    '''

# 13. Capitalize first letter of every word

# Without using .title():

'''s = "python is a programming language"
res = " "
for i in s.split():
    res = res + i.title() + " "
print(res)  ''' 

'''s = "python is a programming language"

res = " "
for i in s.split():
    res = res + i[0].upper() + i[1:] + " "
print(res)    
'''


# 14. Find second highest occurring character

'''s = "mississippi"

second_heigh = 0
for i in s:
    if s.count(i) > second_heigh:
        second_heigh = s.count(i)
        res = i       
print(res,":",second_heigh)
'''

# 15. Replace only first occurrence

'''s = "python python python"

print(s.replace("python","java",1)) '''

# 20. Remove all vowels without using replace()

# s = "programming"
'''res = " "
for i in s.upper():
    if i in "AEIOU":
        continue
    res = res + i
print(res)'''


# 18. First non-repeating character

'''s = "aabbcddee"

for i in s:
    if s.count(i) == 1:
        print(i)
        break'''

'''s = "python is easy python is powerful python"
count = 0
for i in s.split():
    if i == "python":
        count = count + 1
print(count)        
    '''



'''for i in range(96,123):
    print(chr(i))

a = "accdea"
print(sorted(a))'''

'''print()
a = "accdea"
a = list(a)
print(type(a))
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)  
print(" ".join(a))'''         
#     print(ord(i))
#     order = order + i
# print(order)

a = ["apple", "banana", "mango"]

x = a.pop(1)

print(x)
print(a)


    
       









