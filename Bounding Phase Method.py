import numpy as np

def fu(x):
    if(x==0):
        x=np.divide(1,np.power(10,12))
    f=float(np.add(np.power(x,2),np.divide(54,x)))
    return f

def delta():
    flag=0
    while(flag==0):
        x0=float(input("Enter the Initial Guess: "))
        dx=float(input("Enter the dx: "))
        if(fu(x0-np.abs(dx))>=fu(x0) and fu(x0)>=fu(x0+np.abs(dx))):
            flag+=1
            return x0,dx
        elif(fu(x0-np.abs(dx))<=fu(x0) and fu(x0)<=fu(x0+np.abs(dx))):
            flag+=1
            return x0,-dx

x0,dx=delta()
k=0
flag=0
i=0

while(flag==0):
    x1=np.add(x0,np.multiply(np.power(2,k),dx))
    if(fu(x1)<fu(x0)):
        k+=1
        x0=x1
        x1=np.add(x0,np.multiply(np.power(2,k),dx))
        print("Iteration ",i+1,": x0: ",x0," and x1: ",x1)
        
    else:
        print("Minimum lies in (",np.around(np.subtract(x0,np.multiply(np.power(2,k-1),dx)),2),",",x1,")")
        flag+=1
    i+=1
print("No.of Iterations performed:",i)