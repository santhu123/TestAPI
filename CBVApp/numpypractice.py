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