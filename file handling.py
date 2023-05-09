with open(r"C:\Users\91953\OneDrive\Desktop\text.txt","r") as f:
    b=f.readline().split(",")
    c=0
    cu=f.read().split("\n")
    d=[]
    
    for i in cu:
        k={}
        m=0
        B=i.split(",")
        for j in b:
            if B[m].isdigit():
                k[j.strip("\n") ]=int(B[m])
                m=m+1
            else:
                k[j]=B[m]
                m=m+1
        d+=[k]
print(d)

with open(r"C:\Users\91953\OneDrive\Desktop\text.txt","a") as fa:
    for i in d:
        k=fa.write("\n"+str(i))

        
    
 
