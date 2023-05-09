#logic 1
x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[9,8,7],[6,5,4],[3,2,1]]
li=[]
c=0
for i in range(len(x)):
    k=[]
    for j in range(len(x)):
        k+=[x[i][j]+y[i][j]]
    li+=[k]
print(li)
    
    
