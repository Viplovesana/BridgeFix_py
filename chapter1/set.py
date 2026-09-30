# SET   -------------------

fruits = {"apple","banana","orange"}

# Methods of set ------
'''
fruits.add("mango")
print(fruits)'''

'''fruits.update(["grapse","mango"])
print(fruits)'''

'''fruits.remove("orange")
print(fruits)'''

'''fruits.discard("apple")
print(fruits)'''

'''x = fruits.pop()
print(x)'''

'''fruits.clear()
print(fruits)'''

# print(fruits)

#  ------METHAMATICAL METHODS OF SET----------------

'''a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a|b)       ''' # gives the unique element in set

'''a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.intersection(b))
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a&b) '''    # return the common element from the list
'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.difference(b))
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b) '''    # return what ele have inside in the list one and not in list2

'''a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.symmetric_difference(b))''' #it will return every element except repeted

# Cheaking MEthods ------------------

'''a = {1,2}
b = {1,2,3,4}
print(a.issubset(b))'''# Kya main doosre ke andar hoon?	

'''a = {1,2,3,4}
b = {1,2}
print(a.issuperset(b))'''#Kya doosra mere andar hai?

'''a = {1,2,3}
b = {4,5,6}
print(a.isdisjoint(b))'''#Kya dono me kuch bhi common nahi?


# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# result = set(a).difference(b)
# print(result)


'''a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

res = set(a).union(b)
print(res)'''

'''a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

res = set(a).intersection(b)
print(res)'''

# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7,8]

# res = set(a).symmetric_difference(b)
# print(res)


