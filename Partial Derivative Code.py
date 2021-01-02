from sympy import Symbol, Derivative
from sympy import *
x1= Symbol('x1')
x2= Symbol('x2')

fu=fu= ((((x1)**2+x2-11)**2)+(((x2)**2+x1-7)**2))
a=1
b=-1

p11=Derivative(fu,x1,2).doit()
p22=Derivative(fu,x2,2).doit()
p12=Derivative(fu,x1,x2).doit()

print(p11)
print(p22)
print(p12,"\n")

f1=Derivative(fu,x1).doit()
f2=Derivative(fu,x2).doit()

print(f1)
print(f2,"\n")

print("f(x1,x2):",fu,":",fu.evalf(subs={x1:a,x2:b}))
print(p11.evalf(subs={x1:a,x2:b}))
print(p22.evalf(subs={x1:a,x2:b}))
print(p12.evalf(subs={x1:a,x2:b}))


print(f1.evalf(subs={x1:a,x2:b}))
print(f2.evalf(subs={x1:a,x2:b}))

