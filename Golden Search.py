import numpy as np

def fu(x):
    if(x==0):
        x=np.divide(1,np.power(10,12))
    f=float(x**3 - 6*(x**2) + 9*x+6)
    return f

def fuw(w,a,b):
    x=float(a + w*(b-a))
    return fu(x)

a=float(input("Enter a: "))
b=float(input("Enter b: "))
e=float(input("Enter the Termination Factor: "))
print("\n")


L0=b-a

i=0
aw=0
bw=1
L=bw-aw
while(np.abs(L)>e):
    
    x1=float(aw+(0.618)*L)
    x2=float(bw-(0.618)*L)
    x1=np.around(x1,3)
    x2=np.around(x2,3)
    fx1=fuw(x1,a,b)
    fx2=fuw(x2,a,b)
    print("Iteration",i,": (aw,bw): (",aw,",",bw,") L:",L)
    print("w1: ",x1," w2: ",x2)
    print("f(w1): ",np.around(fx1,4)," f(w2): ",np.around(fx2,4))
    
    if(fx1>fx2):
        aw=aw
        bw=x1
        L=bw-aw
    elif(fx1<fx2):

        aw=x2
        L=bw-aw
    else:
        aw=x1
        bw=x2
        L=bw-aw
    print("Therefore (aw,bw): (",aw,",",bw,")")
   
    
    print("\n")
    i+=1
print("No.of Iterations performed:",i)
print("Minimum lies at (",(b-a)*aw,",",(b-a)*bw,")")