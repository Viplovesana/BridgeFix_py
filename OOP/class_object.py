#   HARIOMM------

# class MyClass:
#     x = 5
#     y = 6
#     z = 7
# ob1 = MyClass()
# # del ob1
# print(ob1.x)
# ob2 = MyClass()
# print(ob2.y)
# ob3 = MyClass()
# print(ob3.z)

'''class Student():
    name = "viplove sana"
    age  = 23
s1 = Student()
print(s1.name,s1.age)    
print(s1.age)    '''

# ---------------------------------------------------

'''
class Student():
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

stu = Student("Viplove",23,"Python")
print(f"My name is {stu.name}")
print(f"I am {stu.age} year old")
print(f"i am doing {stu.course}")

stu2 = Student("Rohan",22,"Java")
print(f"My name is {stu2.name}")
print(f"I am {stu2.age} year old")
print(f"i am doing {stu2.course}")'''

# ---------------------------------------------------

'''class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
    def display(self):
        print(self.name)    
        print(self.salary)    
        print(self.department)    
emp = Employee("Viplove Sana",50000,"Python Devloper")
emp.display()
'''

# ------------------------------------------------------

'''class BankAccount():
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def showbalance(self):
        print(self.balance)

    def deposit(self,amount):    
        self.balance = self.balance + amount

    def withdraw(self,wamount):
        self.balance = self.balance - wamount

acc1 = BankAccount("Viplove",10000)     
acc2 = BankAccount("Rohan",20000)
acc1.showbalance()   
acc1.deposit(5000)
acc1.showbalance()   
acc2.withdraw(3000)
acc2.showbalance()  ''' 

# ----------------------------------------------------
# ----INSTANCE VARIABLE-------------------------------

'''class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj1 = Employee("Viplove Sana",23)
print(obj1.name,obj1.age)        
obj2 = Employee("aditya Thakur",22)        
print(obj2.name,obj2.age)        
'''

# ----------------------------------------------------
# ----CLASS VARIABLE----------------------------------


'''class Student:
    collage = "RGPV"
    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)
        print(self.collage)

stu = Student("Viplove")  
stu.display()          
'''

'''class Employee:
    company = "BridgeFix"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def Company(self):
        print(self.company)

stu1 = Employee("Viplove",50000)  
print(stu1.name,stu1.salary)
stu2 = Employee("Rohan",30000)  
print(stu2.name,stu2.salary)
stu1.Company()
stu2.Company()
print(Employee.company)
'''

'''
class Employee:
    company = "BridgeFix"
    def __init__(self,name):
        self.name = name
emp1 = Employee("Viplove")        
emp2 = Employee("Rohan")
emp1.company = "google"

print(emp1.name)
print(emp1.company)
print(emp2.name)
print(emp2.company)
print(Employee.company)'''



'''class Employee:
    company = "BridgeFix"
    def __init__(self,name):
        self.name = name
emp1 = Employee("Viplove")        
emp2 = Employee("Rohan")
emp1.company = "TCS"
Employee.company = "google"
print(emp1.name)
print(emp1.company)
print(emp2.name)
print(emp2.company)
print(Employee.company)'''

'''class Employee:
    company = "BridgeFix"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def change_company(cls):
        cls.company = "TCS"
       
e1 = Employee("viplove",500000)
e2 = Employee("Rohan",300000)
Employee.change_company()
# e1.change_company()
# e2.change_company()
print(e1.company)
print(e2.company)v            
print(Employee.company)'''



# -----------------------------------------------------------------------
# types of variables-----------------------

# isinstance variable---

'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
e1 = Employee("Viplove",60000)
print(e1.name)
e2 = Employee("Rohan",50000)
print(e2.name)'''

# class variable---'

'''class Employee:
    company = "BridgeFix"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
e1 = Employee("Viplove",60000)
print(e1.company)
e2 = Employee("Rohan",50000)
print(e2.company)'''

# types of methods-------------------------------------------

# instance method --------

'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(self.name)
        print(self.salary)  

emp = Employee("viplove sana",50000)
emp.display()'''

# class method --------------

'''class Employee:
    company = "Google"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod    
    def display(cls):
        cls.company = "BridgeFix"
        
emp1 = Employee("viplove sana",50000)
emp2 = Employee("yashraj thakur",40000)
Employee.display()
print(emp1.company)
print(emp2.company)
'''

# static method ---------- 

'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @staticmethod
    def display(a,b):
        return a+b
emp=Employee("viplove sana",50000)
print(emp.name,emp.salary)
print(Employee.display(10,20))'''




