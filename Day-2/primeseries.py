#input:10
#output:2 3 5 7
data=[]
n=int(input())
for r in range(1,n+1):
    count=0
    for i in range(1,r+1):
        if (r%i==0):
            count=count+1
    if(count==2):
        data.append(r)
print(data)



            
        

