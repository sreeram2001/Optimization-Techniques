import numpy as np

def fu(x):
    if(x==0):
        x=np.divide(1,np.power(10,12))
    f=float(np.power(x,3)- 6*(x**2) + 9*x + 6 )
    return f

a=float(input("Enter a: "))
b=float(input("Enter b: "))
e=float(input("Enter the Termination Factor: "))
L0=b-a
L=L0
i=0
while(np.abs(L)>e):
    xm=np.divide(np.add(a,b),2)
    fxm=fu(xm)
    x1=np.add(a,np.divide(L,4))
    x2=np.subtract(b,np.divide(L,4))
    fx1=fu(x1)
    fx2=fu(x2)
    
    if(fx1<fxm):
        b=xm
        xm=x1
        L=b-a
    elif(fx2<fxm):
        a=xm
        xm=x2
        L=b-a
    else:
        a=x1
        b=x2
        L=b-a
    print("Iteration ",i+1,": (a:",a,",b:",b,") L:",L)
    i+=1
print("No.of Iterations performed:",i)