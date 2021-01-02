import numpy as np
import control

def fu(x):
    x1=x[0]
    x2=x[1]
    f=float(((x1**2 +x2-11)**2+(x2**2 + x1 - 7)**2))
    return f

def xn(y,b,xl,xg,xh,xc,xr):
    xnew=xr
    if(fu(xr)<fu(xl)):
        xnew=(1+y)*xc-y*xh
    elif(fu(xr)>=fu(xh)):
        xnew=(1-b)*xc+b*xh
    elif(fu(xr)>fu(xg) and fu(xr)<fu(xh)):
        xnew=(1+b)*xc-b*xh
    return xnew

def Termination(x,xc,e):
    Q=float(0)
    for i in range(3):
        Q+=np.divide((fu(x[i])-fu(xc))**2,4)
    Q=np.sqrt(Q)    
    print("Termination Value (Q): ",np.around(Q,3))
    if (Q<e):
        return 1
    else:
        return 0

def fux(x):
    a=np.zeros((3,2))
    f1=fu(x[0])
    f2=fu(x[1])
    f3=fu(x[2])
    f=[f1,f2,f3]
    f.sort()
    
    if(f1==f[0]):
        
        a[0]=x[0]
   
    elif(f2==f[0]):
       
        a[0]=x[1]
    
    elif(f3==f[0]):
        
        a[0]=x[2]
    
    if(f1==f[1]):
        
        a[1]=x[0]
    
    elif(f2==f[1]):
       
        a[1]=x[1]
    
    elif(f3==f[1]):
        
        a[1]=x[2]
    
    if(f1==f[2]):
        
        a[2]=x[0]
    
    elif(f2==f[2]):
        
        a[2]=x[1]
    
    elif(f3==f[2]):
        
        a[2]=x[2]
        
    return a

"""y=float(input("Enter gamma:"))
b=float(input("Enter beta: "))
e=float(input( "Enter the termination factor: "))"""

y=2.6
b=0.5
e=0.001
x=np.zeros((3,2))
x[0]=[1,0]
x[1]=[1,1]
x[2]=[2,0]

flag=0
k=0
while(flag==0):
    print("\nIteration",k+1,":")
    for j in range(3):
        print("x_",j+1,": ",x[j],"f(x_",j+1,"): ",fu(x[j]))

    xl,xg,xh=fux(x)

    xc=(xl+xg)/2
    print("xc: ",xc)
    xr=2*xc-xh
    xnew=xr
    xnew=xn(y, b, xl, xg, xh, xc, xr)
    a=[xl,xg,xnew]
    x=fux(a)

    for j in range(3):
        print("f(x_",j+1,"): ",fu(x[j]))
    print(fu(xc))
    flag=Termination(x,xc,e)
    print(x)
    k+=1
    


