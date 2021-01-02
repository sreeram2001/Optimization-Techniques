import numpy as np
from sympy import Symbol, Derivative
from sympy import *


x= Symbol('x')
y= Symbol('y')
fu= 2*x**2+2*y**2-x*y+2*x-y+5

def Ji(a,b):
    J=np.zeros([2,2])
    p11=Derivative(fu,x,2).doit().evalf(subs={x:a,y:b})
    p22=Derivative(fu,y,2).doit().evalf(subs={x:a,y:b})
    p12=Derivative(fu,x,y).doit().evalf(subs={x:a,y:b})
    p21=Derivative(fu,y,x).doit().evalf(subs={x:a,y:b})
    J[0][0]=p11
    J[0][1]=p12
    J[1][0]=p21
    J[1][1]=p22
    print(J)
    print("\n",np.linalg.inv(J))
    return np.linalg.inv(J)

def fi(a,b):
    fi=np.zeros([2,1])
    f1=Derivative(fu,x).doit().evalf(subs={x:a,y:b})
    f2=Derivative(fu,y).doit().evalf(subs={x:a,y:b})
    fi[0][0]=f1
    fi[1][0]=f2
    print("\n",fi)
    return fi

x1=float(input("Enter x1: "))
x2=float(input("Enter x2: "))

f=np.zeros([2,2])
f=Ji(x1,x2)

g=np.zeros([2,1])-0.270844
g=fi(x1,x2)

X1=np.zeros([2,1])
X1[0]=x1
X1[1]=x2
X2=np.zeros([2,1])
X=np.dot(f,g)
X2[0]=X1[0]-X[0]
X2[1]=X1[1]-X[1]

print("\n",X2)


