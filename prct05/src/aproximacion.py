#!/usr/bin/python
PI = 3.14159265358979323846264338327950288
n = int(raw_input('Valor de n: '))
sumatorio=0
for i in range (1,n+1):
    a= float(i-1)/n
    b= float(i)/n
    x_i=(i-0.5)/float(n)  
    fx_i=4/(1+x_i**2)  
    print 'subintervalo (%.5f,%.5f) x_i: %.5f fx_i: %.5f'%(a,b,x_i,fx_i)  
    sumatorio+=fx_i
pi=sumatorio/n
print 'El valor pi es %.35f' %pi
print 'El valor de pi con 35 decimales es %.35f' %PI
