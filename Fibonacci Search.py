import numpy as np

def F(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 1
    # Second Fibonacci number is 1 
    elif n==2: 
        return 2
    else: 
        return F(n-1)+F(n-2)
    
    
    
def fu(x):
    if(x==0):
        x=np.divide(1,np.power(10,12))
    f=float(2*(np.power(x,3)/3) + 5*x - np.exp(x))
    return f


a=float(input("Enter a: "))
b=float(input("Enter b: "))
e=float(input("Enter the Termination Factor: "))
n=int(input("Enter desired number of function evaluations: "))
print("\n")


L=b-a

i=0
k=2


while(k!=n+1):
    
    Lk=np.multiply(np.divide(F(n-k+1),F(n+1)),L)
    x1 = a + Lk
    x2 = b - Lk
    print()
    fx1=fu(x1)
    fx2=fu(x2)
    
    if(fx1<fx2):
        b=x2
        
        Lk=b-a
   
    elif(fx2<fx1):
        a=x1
        
        Lk=b-a
    
    else:
        a=x1
        b=x2
        Lk=b-a
    
    print("Iteration ",i+1,":","\nF(n-k+1):",F(n-k+1)," F(n+1):",F(n+1),"L:",L,"Lk:",Lk,"\n(x1,x2):(",x1,",",x2,")","\n(a,b):(",a,",",b,") ")
  
    
    i+=1
    k+=1
    
    
print("\nNo.of Iterations performed:",i)
print("Final interval lies at (",a,",",b,") at the end of", i," iterations.")