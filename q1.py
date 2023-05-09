#logic 1
a=[(),("ram","15","8"),(),("laksman","sita"),("krishna","akbar","45"),(","),()]
for i in a:
    if len(i)>=1:
        continue
    else:
        a.remove(i)
print(a)

# logic 2
a=[(),("ram","15","8"),(),("laksman","sita"),("krishna","akbar","45"),(","),()]
li=[]
for i in a:
    c=0
    for j in i:
        c+=1
    if c > 0:
        li+=[i]
print(li)
    
