import numpy as np

def fu(x):
    f=float(np.add(np.power(x,2),np.divide(54,x)))
    return f

def fu1(x,dx):
    f1=float(np.divide((fu((x+dx))-fu((x-dx ))),(np.multiply(2,dx))))
    return f1

dx=0.00001
e=float(input("Enter the termination factor: "))
a=float(input("a:"))
b=float(input("b:"))
flag=1
i=0

while(flag==1):
    print("\nIteration",i+1)
    print("a:",a,"b:",b)
    print("f'(a):",fu1(a,dx),"f'(b):",fu1(b,dx))
    z=float(b-(fu1(b,dx)/((fu1(b,dx)-fu1(a,dx))/(b-a))))
    print("z:",z," f'(z):",fu1(z,dx))
    if(np.abs(fu1(z,dx))<e):
        flag=0
    if(fu1(z,dx)<0):
        a=z
    elif(fu1(z,dx)>0):
        b=z
    i+=1
        