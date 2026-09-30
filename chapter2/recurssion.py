
# ===RECURSSION====================================
# l = []
# def sum(n):
#     if n == 0:
#         return
#     print(n)
#     l.append(n)

#     sum(n-1)

#     l.append(n)
#     print(n)
# sum(4)
# print(l)

# def countdown(n):
#     if n == 0:
#         return n
#     return n + countdown(n-1)
   
# print(countdown(4))

# 6. Ek aur simple example: 1 se N print karna

# def num(n):
#     if n == 0:
#         return 
#     num(n-1)
#     print(n)
# num(10)    

'''
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n)


print_numbers(5)
bhai isme thoda samjhna hai kese ho raha hai n-1 9,8,7,6.... ho raha hai to uske niche print karne se 1,2,3,4 kese'''

# def fact(n):
#     if n == 0:
#         return 0
#     return n * fact(n-1)

# res = fact(5)
# print(res)

# Q5. Print N times.............

'''def func(n):
    if n == 0:
        return    
    print("hello")
    func(n-1)
func(5)'''

# Q6. Print even numbers

'''def func(n):
    if n == 11:
        return
    if n%2==0:
        print(n)
    func(n+1)
func(1)
'''
# Q7. Print odd numbers

'''def func(n):
    if n == 0:
        return
    func(n-1)
    if n%2!=0:
       print(n)
func(10)         
'''
# Q9. 1 se n tak sum
'''def func(n):
    if n == 0:
        return 0
    return n + func(n-1)
r = func(5)
print(r) '''

'''def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

res = fact(5)
print(res)
'''
# Q11. n ki power calculate karo
# power(2, 5)
'''
def power(a,n):
    if n==0:
        return 1

    return a * power(a,n-1)
print(power(2,5))'''
# ------------------------------------------------
'''def pow(p,n):
    if n == 0:
        return 1
    return p * pow(p,n-1)

print(pow(3,8))'''

# Q12. Number ke digits ka sum
# digit_sum(12345)

# Q12. Number ke digits ka sum
# digit_sum(12345)

'''def func(n):
    if n == 0:
        return 0
    return n%10 + func(n//10)
print(func(12345))'''

# Q13. Number mein kitne digits hain?

'''def func(n):
    if n == 0:
        return 0
    return 1 + func(n//10)
print(func(1234589))    
'''
# Q14. Number reverse karo
# reverse(12345)

# Q15. Number ke digits print karo
# print_digits(12345)

'''def func(n):
    if n == 0:
        return 0
    func(n//10)
    print(n%10)
    
func(12345) '''

# Q23. List ke saare elements print karo
# a = [10, 20, 30, 40, 50]
'''a = [10, 20, 30, 40, 50]
def func(a,i):
    if i == len(a):
        return 0 
    print(a[i])
    func(a,i+1)
func(a,0) ''' 

# reverse order---------------------

'''a = [10, 20, 30, 40, 50]
def func(l,i):
    if i == 5:
        return 0 
    func(l,i+1)
    print(a[i])
func(a,0)'''

# Q25. List ka sum
# a = [1, 2, 3, 4, 5]

'''a = [1, 2, 3, 4, 5]
def sum(l,i):
    if i == 5:
        return 0
    return(a[i]) + sum(l,i+1)
print(sum(a,0))
'''

# Q26. List ka maximum element
'''a = [10, 5, 30, 20, 15]
def max(l,i):
    if i == 5:
        return 0
    maximum = max(l,i+1)   
    if l[i] > maximum:
        maximum = l[i] 
    return maximum    
    
print(max(a,0))   '''


# Q28. List mein even numbers count karo
'''a = [1, 2, 4, 7, 8, 10]

def func(l,i):
    if i == 5:
        return 0
    if l[i]%2 == 0:
        print(l[i])
    func(l,i+1)
    
func(a,0)'''

# Q31. String reverse karo
# reverse("hello")

# def reverse(s,i):
#     if i == len(s):
#         return 0
#     reverse(s,i+1)
#     print(s[i],end=" ")

# reverse("hello",0)

# Q32. String palindrome hai ya nahi?
# "madam"
# a = "madam"
# def func(s,i):
#     if i == len(s):
#         return 0
#     y = s[i]
#     func(s,i+1)
#     x = s[i]
#     if x == y :
#         print("palindrom")
#     else:
#         print("not a palindrom")
# func(a,0)

# Q33. Vowels count karo
'''a = "education"
def func(s,i):
    if i == len(s):
        return 0
    if s[i] in "aeiou":
        print(s[i])
    func(s,i+1)
func(a,0)'''

# # Q34. String mein character count karo
# def count_char(s):
#     if s == 0 :
#         return 0
#     print(s)
#     return 1 + count_char(s//10)


# count_char("banana", "a")       