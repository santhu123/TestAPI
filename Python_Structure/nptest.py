
#No copy 
from re import A
import numpy as np
# a=np.arange(6)
# print("my array:")
# print(a)
# print("id of a array:")
# print(id(a))
# b=a 
# print("my b is:",b)
# print("my b id:",id(b))
# b.shape=3,2
# print("new shape of b:",b)
# print("final",a)
a=np.arange(6).reshape(3,2)
print("my a:",a)
b=a.view()
print("my b is:",b)

print("id of a is:",id(a))
print("id of b is:",id(b))

b.shape=2,3
print("shape b:",b)
print("final a :",a)