#factors of given number
#Test Case-1
#input:15
#output:1 3 5 15
#Test Case-2:
#input:24
#output:1 2 3 4 6 8 12 24
''' muliline comment
        multiline comment '''

num=int(input("Enter num Value "))
for i in range(1,num+1):
    if num%i==0:
        print(i,end=" ")
        
