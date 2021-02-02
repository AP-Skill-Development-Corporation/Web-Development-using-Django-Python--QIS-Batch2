#apssdc
#{'a':1,'p':1,'s':2,'d':1,'c':1}

name =  input("Enter your name")
dict1 = {}
for char in name:
    if char in dict1:
        dict1[char] = dict1[char]+1
    else:
        dict1[char]=1

print(dict1)
