#TestCase-1
#input:5
#input:(x,y):3 5
#output:56 57 58 59 60
#Testcase-2
#input:10
#input:(x,y):3 5
#output:56 57 58 59 60 61 62 63 64 65

#task:
#input:15
#input:x,y:3 5
#output:57 59 61 63 65 67 69 71 73 75 77 79 81 83 85

#Explanation:
''' f(i,x,y)=5*x+3*y+x*y+10+i
        iteration-1:
            f(1,3,5)=5*3+3*5+3*5+10+1 -->56
        iterations:2
            f(2,3,5)=5*3+3*5+3*5+10+2 -->57
        iteration:3:
            f(3,3,5)=5*3+3*5+3*5+10+3 -->58 '''

n=int(input())
x=int(input())
y=int(input())

for i in range(1,n+1):
    expre=5*x+3*y+x*y+10+i
    print(expre,end=" ")
    
