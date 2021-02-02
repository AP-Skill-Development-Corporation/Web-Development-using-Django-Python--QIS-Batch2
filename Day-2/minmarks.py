dict2 = {'pavan':125,"siva":140,'rajesh':189,"vijay":200}
list1 = []
for marks in dict2.keys():
    list1.append(dict2[marks])
min_value = min(list1)

for name in dict2.keys():
    if dict2[name]==min_value:
        print(name)
        
