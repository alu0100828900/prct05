#!/usr/bin/python
n = int(raw_input('Valor de n: '))
sumatorio=0
for i in range (1,n+1):
    a= float(i-1)/n
    b= float(i)/n
    print 'subintervalo (%.5f,%.5f)'%(a,b)  
    x_i=(i-0.5)/float(n)  
    print 'x_i: %f' %x_i  
    fx_i=4/(1+x_i**2)  
    print 'fx_i: %f' %fx_i  
    sumatorio+=fx_i
pi=sumatorio/n
print 'El valor pi es %f' %pi
print 'El valor de pi con 35 decimales es %.35f' %pi
