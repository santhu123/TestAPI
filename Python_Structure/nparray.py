# from ast import Delete
# from itertools import product
# from re import U
# from turtle import dot



# #1 dimensional array
# # a=np.array([1,2,3])

# # print(a)

# ## creating 2 *3dimensional array  
# # arr2=np.array([
# #    [ [1,2,3],
# #     [4,5,6]],
# #    [
# #        [8,9,10],
# #        [5,2,1,65]
# #    ]
# # ])
# # print(arr2)

# # a=np.zeros((2,2))
# # print(a)
# # a1=np.ones((2,2))
# # print(a1)
# # x=1.2
# # a2=np.full((2,2),x)
# # print(a2)

# # d=np.eye(3)
# # print(d)

# ## creatingthe array with random values  
# # e=np.random.randint((2,2))
# # print(e)

# # # np.arrange()
# # f=np.arange(0,30,5)
# # print(f)

# # fd=np.linspace(1,15,3)
# # print(fd)


# # arra2[1,0,2]


# # i=1,j=0,k=2

# Numpy:
#     Linear Algebra
#     distribution
#     vectors  ---dot product,cross product
#     strings  
    
#     Array Manipulation
    
    
# Numpy Linear Algebra: 
#     numpy.linalg

#     dot---dot product of two arrays
#     vdot  --dot product of two vectors  
#     inner --inner product of two arrays  
#     matmul  ---matrix product of two Arrays 
#     determinant --determinant of Array 
#     solve ---solves linear matrix  
#     inv ---multiplicative inverse od the matrix  
    
#  s=hello.santhosha.how.are.U  
#  s.join(".") 
# Numpy:
    
#     add()
#     multiply()  
#     center()
#     capitalize()  
#     title()
#     lower()
#     upper()
#     split()
#     splitlines() 
#     strip()
#     join() 
#     replace()
#     decode()
#     encode()
    


# Array Manipulations in numpy:
     
#      Changing the shapes 
#      1.reshape()
#      2.flat()
#      3.flatten() 
#      4.ravel() --flatten array  
#      Transpose Operations : 
#          1.transpose()
#          2.ndarray()
#          3.rollaxis()
#          4.swapaxis()
         
#     Changing the Dimensions :
#         1.braodcast
#         2.broadcast_to 
#         3.expand_dims 
#         4.squeeze
#     Joining the Arrays :
#         1.concatenate 
#         2.stack 
#         3.hstack 
#         4.vstack 
#     Splitting Arrays: 
#         split 
#         hsplit
#         vsplit
#     Adding and Removing the Elements : 
#         1.resize 
#         2.append 
#         3.insert 
#         4.delete 
#         5.unique 
        
#String Operations in Numpy :
#import numpy as np
# print("Concatenate two strings")

# print(np.char.add(['python'],['lang']))

# print("Concatenate two example")
# # print(np.char.add(['python','java','c'],['lang','lang1']))

# ###Multiply---numpy.char.multiply()
# print(np.char.multiply('python',5))

# ##center  ---numpy.char.center()
# print(np.char.center('Python1',10,fillchar='+'))

# ## Capitalize  --numpy.char.capitalize()

# print(np.char.capitalize('python language'))

### Encode the TSring in numpy  :numpy.char.encode(),decode()

# a=np.char.encode('hello','cp500')
# print(a)
# print(np.char.decode(a,'cp500'))
##  Join Method print

# print(np.char.join(':','dmy'))

# print(np.char.join([':','-'],['dmy','ymd']))

# ## split() 
# print(np.char.split("hello python how are ypou"))
# print(np.char.split('Hyderabad,Chennai,Bangalore',sep=','))


#replace()

import numpy as np

def string_concatenate():
    x="Python "
    y="lang"
    print ("String Concatenation")
    print(np.char.add(["Python "],["lang"]))
    print(np.char.add(x,y))
    print ("================")

def string_mul():
    x="Python "
    print ("String multiply")
    print(np.char.multiply(["Python "],[5]))
    print(np.char.multiply(x,5))
    print(np.char.multiply("Python ",5))
    print ("================")

def string_capitalize():
    x="python is an open source"
    print ("String capitalize")
    print(np.char.capitalize(["python is an open source"]))
    print(np.char.capitalize("python is an open source"))
    print(np.char.capitalize(x))
    print ("================")

def string_title():
    x="python is an open source"
    print ("String title")
    print(np.char.title(["python is an open source"]))
    print(np.char.title(x))
    print ("================")

def string_lower():
    x="Python Is An Open Source"
    print ("String lower")
    print(np.char.lower(["python is an open source"]))
    print(np.char.lower(x))
    print ("================")

def string_upper():
    x="python is an open source"
    print ("String upper")
    print(np.char.upper(["python is an open source"]))
    print(np.char.upper(x))
    print ("================")

def string_count():
    x="python is an open source"
    a=["six","seven","score"]
    print ("String count")
    print(np.char.count(x,"s"))
    print(np.char.count(a,"s"))
    print ("================")

def string_compare():
    a="python language"
    b="python language"
    print ("String compare")
    a=np.char.equal(a,b)
    print(a)
    print ("================")


def string_encode_decode():
    x="python"
    print ("String encode")
    a=np.char.encode('python','cp500')
    b=np.char.encode('python','UTF-8')
    print(a)
    print(b)
    print("&&&&&&")
    print ("String decode")
    print(np.char.decode(a,'cp500'))
    print(np.char.decode(b,'UTF-8'))
    print ("================")

if __name__== "__main__":
    string_concatenate()
    string_mul()
    string_capitalize()
    string_encode_decode()
    string_title()
    string_lower()
    string_upper()
    string_count()
    string_compare()


    
     