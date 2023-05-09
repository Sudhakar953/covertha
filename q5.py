#logic 1
a=input()
if len(a)>=8:
    sm_case=0
    up_case=0
    num=0
    spl_case=0
    for i in a:
        if i.islower():
            sm_case+=1
        elif i.isupper():
            up_case+=1
        elif i.isdigit():
            num+=1
        elif i=="@" or i=="_" or i=="$":
            spl_case+=1
if sm_case>0 and up_case>0 and num>0 and spl_case>0:
    print("accpted")
else:
    print("reenter pin")

#logic 2
    

