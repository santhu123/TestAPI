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
import numpy as np
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


replace()




    
     