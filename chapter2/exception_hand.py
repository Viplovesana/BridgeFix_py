
# EXCEPTION HANDLING ===============================>

# a = 10
# b = 0
# print(a/b)      

# Without try-except------

# print("hi")
# print(10/0)
# print("viplove")

# With try-except: 

'''print("hi")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("viplove")  
'''

# a = int(input("Enter the number :"))
# b = int(input("Enter the number :"))
# try:
#    print(a/b)
# except:
#    print("somthing wwent wrong")   
# print("program is completed")

'''try:
   print(10/0)
except:
    print("cannot divide by zero")  ''' 

'''try:
    x = int(input("Enter the no"))
    y = int(input("Enter the no"))
    print(x/y)

    print(10/2)
except(ZeroDivisionError,ValueError) as msg:
    print(msg)       
# except ZeroDivisionError as msg:
#     print(msg)
 '''


'''try:
    x = int(input("Enter the no"))
    y = int(input("Enter the no"))
    print(x/y)

    print(10/2)
except ZeroDivisionError:
    print(ZeroDivisionError,"cant devided with zero") 
except:
    print("default except:please provide valid input")          
'''

# Case-1: If there is no exception ================================================= 

'''try:
    print("try")
except:
    print("except")
finally:
    print("finally")     '''

# Case-2: If there is an exception raised but handled  =================================================
'''try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print(ZeroDivisionError,"cant devided with zero")
finally:
    print("finally")  '''   

# Case-3: If there is an exception raised but not handled =========================================
'''import os
try:
    print(10/0)
    os._exit(0)
except NameError:
    print("except")
finally:
    print("finally") 
'''

# ===============================================
'''
import os
try:
    print("hii")
    print("viplove sana")
    
except ZeroDivisionError:
    print("except")
finally:
    print(10/0) 
'''

'''a = [1,2,3,5,7]
b = [1,5,3,2,7]'''
'''if len(a) == len(b):
    for i in a:
        if a.count(i) == b.count(i):
            print("same")
            
        else:
            print("not same")    
else:
    print("not same")    '''

# try:
#     print("try")
# except ZeroDivisionError as msg:
#     print(ZeroDivisionError,"cant devide by zero")
# finally:
#     print(10/0) # it will raise a abnormal termination-------------------------
#     print("finally")        


# try:
#     print("outer try")
#     try:
#         print(10/0)
#     except:
#         print("inner except")
#     finally:
#         print("inner finally")
# except:
#     print("outetr except")
# finally:
#     print("outer finally")  

#  ELSE WITH TRY EXCEPT BLOCK======================================================

# try:
#     # print("try")                  
#     print(10/0)
# except:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")                          

# try:
#     print("try")                  
# except:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")

'''def func():
    try:
        print("try")
    except ZeroDivisionError:
        print(ZeroDivisionError,"cant devided by zero")   
    else:
        return "else"    
    finally:
        return "finally"
print(func())    
    '''

def calculator():
    try:
        a = int(input("enter a 1st number :- "))
        operator = input("select operator (+,-,*,/) :- ")
        b = int(input("enter a 2nd number :- "))

        if operator not in '+,-,*,/':
            raise ValueError("incorect operator")

        elif operator == '+':
            result = a+b

        elif operator == '-':
            result = a-b

        elif operator == '/':
            result = a/b

        elif operator == '*':
            result = a*b

        # x = 7/0

    except ValueError as e:
        return str(e)    
    
    # except ValueError:
    #     return "enter only numbers "

    # except ZeroDivisionError:
       
        # try:
        #     x = 7/0
        # except ZeroDivisionError:
        #     return "cannot divide by zero"

    except ZeroDivisionError:
         return "cannot divide by zero"

    else:
        print(result)


    finally:
    
        print("=================== Execution is coompleted ===================")


calculator()