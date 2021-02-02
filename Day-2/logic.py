#input:5
#output:11 17 23 29 35

#Explanation:
''' f(x)=4*x+2*x+5
    f(1)=4*1+2*1+5-->11
    f(2)=4*2+2*2+5-->17
    f(3)=4*3+2*3+5-->23
    f(4)=4*4+2*4+5-->29
    f(5)=4*5+2*5+5-->35 '''


n=int(input("Enter n value"))
for x in range(1,n+1):
    expre=4*x+2*x+5
    print(expre,end=" ")

