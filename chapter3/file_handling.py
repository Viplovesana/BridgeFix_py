

import os
def outer_func(main_func):
    def inner_func(z):
        if os.path.getsize(z) == 0:
            return 
        else:    
            print("file is not empty")
    
    return inner_func
@outer_func
def main_func(a):
    with open(a, 'r') as file:
        x = file.read()
    return x
a=r"C:\Users\LENOVO\OneDrive\Desktop\bridgefix\chapter3\file.txt"
main_func(a)

# for creating the new file ..........................
'''with open ("newFile2.txt","x") as file:
    file.write("hey buddy")
'''

# for read the file ..................................
'''with open ("newFile2.txt","r") as file:
    x=file.read()
    print(x)'''

# for write the file ..................................    
'''with open ("newFile2.txt","w") as file:
    file.write("how are you") # this will overwrite the code or file 
        '''
# for append the file ..................................
'''with open ("newFile2.txt","a") as file:
    x=file.write(" viplove ,i hope all good")'''

# for read+(r+) the file ..................................
'''with open ("newFile2.txt","r+") as file:
  
    file.write("hey this is new data") '''  


# for write+(w+) the file ..................................
'''with open ("newFile.txt","w+") as file:
      
    # file.write("hey") 
    print(file.tell())
    print(file.seek(0))
    x = file.read() 
print(x)  '''  


# for append+(a+) the file ..................................
'''with open ("newFile.txt","a+") as file:
    file.seek(0)
    x = file.read()
    print(x)
    file.write(" , how are you")'''


# for write+text (wt) the file ..................................
'''with open ("newFile.txt","wt") as file:
    file.write("hey bro this your time")  ''' 

#  SAME FOR APPEND + TEXT 


# d = { "name":"viplove","city":"dewas"}
# d["name"] = "rohan"         
# print(d)


'''with open("newFile.txt","r") as file:
    x = file.read()
    print(x)'''


# data = ["Python\n","Django\n","DRF\n"]
# with open("newFile.txt","a+") as file:
#     file.writelines(data)


# ================= FILE CHEAKING =========================================

'''import os

x = os.path.exists("oldFile.txt")
print(x)

os.remove("newFile2.txt")'''

# ============== FILE HANDLING WITH EXCEPTION =============================================================

'''try:
    with open("file2.txt") as file:
        print(file.read())
except:
    print("Except for try :- file dose not exist") 
finally:
    print("finally")
    with open("file.txt") as file:
            print(file.read())    
'''

# ===  FILE HANDLING WITH TELL AND SEEK METHOD ====================================================
'''
with open("file.txt") as file:
        print(file.read()) 
        print(file.tell())
        print(file.seek(12))
        print(file.read()) '''


# ===  FILE HANDLING WITH JSON MODULE ====================================================

'''# import json

# employee = {
#     "name":"viplove sana",
#     "city":"dewas"
# }
# with open("file.txt","w") as file:
#     json.dump(employee,file)

# with open("file.txt","r") as file:
#     x = json.load(file)
#     print(x)
'''

# ===  FILE HANDLING WITH PICKLE MODULE ====================================================

'''# import pickle
# data = ['viplove',24,'python','dewas']
# with open('file.txt','wb') as file:            #pickle.dump(convert python object into binary object)
#     pickle.dump(data,file)'''

'''# with open('file.txt','rb') as file:
#     x = pickle.load(file)                  #pickle.dump(convert binary object into again python object)
#     print(x)
'''




 


