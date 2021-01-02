import matplotlib.pyplot as plt
import numpy as np
from sympy import *
x, y, z,s = symbols('x y z s')
init_printing(use_latex=True)
"""
import control

n1=int(input("Enter the order of the array of numerator:"))
n2=int(input("Enter the order of the array of denominator:"))
num=np.zeros(n1+1)
denum=np.zeros(n2+1)
print("Enter the co.efficients for the numerator:")

for i in range(0,n1+1,1):
    print(i,"th coefficient:")
    num[i]=float(input())

print("Enter the co.efficients for the denominator:")

for i in range(0,n2+1,1):
    print(i,"th coefficient:")
    denum[i]=float(input())

H=control.TransferFunction(num,denum)
print(H)"""
    
def fu(x):
    #f=float(np.real(H(x)))
    f=float(np.power(x,3) - 6*(x**2) + 9*x + 6)
    return f

def fu1(x,dx):
    f1=float(np.divide((fu((x+dx))-fu((x-dx ))),(np.multiply(2,dx))))
    return f1

def fu2(x,dx):
    f2=float((np.divide(fu((x+dx))+fu((x-dx))-2*fu((x )),(np.power(dx,2 )))))
    return f2

e=float(input("Enter the Termination factor(from 10^-4 till 10^-10):"))
x=float(input("Enter Initial Guess: "))
flag=1
i=0

while(flag==1):
    dx=float(np.multiply(0.01,x))
    print("\nx:",i+1,":",x," dx:",dx,"\nf'(x):",fu1(x,dx),"f''(x):",fu2(x,dx))
    x= float(x-( fu1(x,dx)/fu2(x,dx)))
    dx=float(np.multiply(0.01,x))
    print("x:",i+2,":",x,"f'(x):",fu1(x,dx))
    i+=1
    if(np.abs(fu1(x,dx))<e):
        flag=0
    