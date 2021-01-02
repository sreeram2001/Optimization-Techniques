import numpy as np

def fu(x):
    if(x==0):
        x=np.divide(1,np.power(10,12))
    f=float(np.add(np.power(x,2),np.divide(54,x)))
    return f

a=float(input("Enter a: "))
b=float(input("Enter b: "))
n=int(input("Enter the number of intermediate points: "))
dx=float(np.divide(np.subtract(b,a),n))
dx=np.abs(dx)
flag=0
i=0
x1=a
x2=x1+dx
x3=x2+dx
while(flag==0):
    if(fu(x1)>=fu(x2) and fu(x2)<=fu(x3)):
        flag+=1
        print("Minimum lies in (",x1,",",x3,")")
    x1=x2
    x2=x1+dx
    x3=x2+dx
    if(x3>b):
        flag+=1
        print("No minimum or minimum lies at boundary points ",a,"and",b)
    i+=1
print("No.of iterations taken:",i)
l = ( 2/n ) * ( b - a )
print("Length :",l)