n=int(input())
od=input()
b=""
for  i in range(ord(od),(ord(od)+n)):
    n=n-1
    b+=chr(i)+" "
for i in range(2,len(b)+1,2):
    n=n+1
    print(" "*n+b[0:len(b)-i])
'''a="A B C D E F G H I J K L M N O P Q R S T U V U X Y Z "
b=int(input())
n=b
for i in range(0,b*2,2):
    n=n-1
    print(" "*(n)+a[0:i+1])'''

