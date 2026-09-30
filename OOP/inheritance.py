
'''class Parent:
    def show(self):
        print("i am parent")
class Child(Parent):
    pass
ch = Child()
ch.show()
'''

'''class Employee:
    def login(self):
        print("login")
    def logout(self):
        print("logout")
class Developer(Employee):
    pass
d = Developer()
d.login()
d.logout()
'''

'''
class Student:
    school = "ABC School"

    def __new__(cls):
        print("I AM CREATING A OBJECT ---------")
        # return super().__new__(cls)
        return "ME vip hoo"

    def __init__(self):
        print("I am INITIalizing object..........")

Student()

print(Student())'''

'''class Parent:
    def show(self):
        print("parent method")

class Child(Parent):
    pass
p1 = Child()
p1.show()'''

# class Parent:
#     def __init__(self):
#         self.name = "viplove"
# class Child(Parent):
#     def __init__(self):  
#         super().__init__() 
#         self.age = 23
# p = Child()
# print(p.age)
# print(p.name)

# Single Inheritance -----------------------------------------------

'''class Parent:
    def house(self):
        print("this is parent house")
class Child(Parent):
    def bike(self):
        print("child bike")
c = Child()
c.bike()        
c.house()        
'''

# 2. Multilevel Inheritance----------------------------------------------

'''class GrandFather:
    def house(self):
        print("this is my house")
class Father(GrandFather):        
    def car(self):
        print("this is my car")
class Son(Father):        
    def bike(self):
        print("this is my bike")
s = Son()    
s.bike()    
s.car()    
s.house() '''   

  
# 3. Multiple Inheritance--------------------------------------------------
  
'''class Father:
    def food(self):
        print("Father feeding")
class Mother:
    def love(self):
        print("mother loving")
class Child(Father,Mother):
    pass
c = Child()
c.food()                
c.love()        '''        


# 4. Hierarchical Inheritance--------------------------------------------------


'''class Parent:
    def Father(self):
        print("gives feed and love")
class Child1(Parent):
    def son(self):
        pass
class Child2(Parent):
    def daughter(self):
        pass
c1 = Child1()
c1.Father()    
c2 = Child2()
c2.Father()    
         '''


# 5. Hybrid Inheritance-------------------------------------
'''
class Father:
    def house(self):
        print("father house")
class Mother(Father):
    def love(self):
        print("giving love and care")
class Child(Father):
    def son(self):
        print("i am the bos of house")
class Animal(Mother,Child):
    def dog(self):
        print("house member")
c = Child()
m = Mother() 
d = Animal()
c.house()
m.love()
m.house()
d.dog()
d.love()
d.son()'''


# ---INHERITENCE WITH SUPER() METHOD-------------------------------------------
 
'''class Parent:
    def __init__(self):
        print("hey i am you papa")
class Child(Parent):
    def __init__(self):
        # super().__init__()
        print("give me some sunshine")    
c = Child()
'''

# Q3. Parent method call--------------------------------------------
'''
class Parent:
    def show(self):
        print("parent show")
class Child(Parent):
    def show(self):
        super().show()
        print("child show")
c = Child()
c.show()
'''

# Q4. Parent variable access----------------------------------------

'''
class Manager:
    company = "TCS"
class Employee:
    company = "Google"
    
class Records(Manager,Employee):
    def show(self):
        print(super().company)
        print("i am the Employee")
r = Records()
r.show()  '''      


# Super with Constructor + Arguments---------------------------------------------

'''class Parent:
    def __init__(self,name):
        self.name = name
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
c = Child("viplove",23)
print(c.name)      
print(c.age)      
'''

# Same variable overwrite------------------------------------------

'''class Parent:
    def __init__(self):
        self.name = "Parent"
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = "Child"
c = Child()
print(c.name) '''


# ---------variable excess by super()-----------------------------------------------------------

'''class Employee:
    name = "Viplove sana"
    def __init__(self,age):
        self.age = age 
    def show(self):
        super().show()
        print("hey i am the employee")
class Manager:
    def show(self):
        print("i am the manager")
class Person(Employee,Manager):
    def __init__(self, age):
        super().__init__(age)
    def show(self):
        super().show()
        print(super().name)
        print("i am the man")  
p = Person(23)
p.show()   
print(p.age)
'''

class Parent:
    def show():
        print("Parent")
class Child:
    def show():
        print("Child")
c = Child()
c.show()        

