import numpy as np
import math as m
import matplotlib.pyplot as plt
Genuine = []
Imposter = []
listx = []
listy = []
listTPR = []
listFPR = []
listFNR = []
x = 0
X = 0
y = 0 
thre = float(input('enter threshold value in range 0 to 100:'))
for i in range(1000000):
    if x<= thre:
       p = m.erf(0.316*x-0.899)/2+0.045
       listTPR.append(p)
       listFNR.append(1-p)
       p = m.erf(0.1825*x-1.8)/2
       listFPR.append(p)
    x = x+0.00001
for i in range(1000000):
    if X<=thre:
       a = 1/m.sqrt(10*m.pi)
       b = m.exp(-(((X-20)/(4*m.sqrt(5)))**2))
       Genuine.append(a*b)
       listx.append(X)
    X = X +0.001
for j in range(1000000):
    if y<=thre:
       c = 1/m.sqrt(30*m.pi)
       d = m.exp(-(((y-60)/(4*m.sqrt(15)))**2))
       Imposter.append(c*d)
       listy.append(y)
    y = y +0.001
plt.plot(listx,Genuine)
plt.plot(listy,Imposter)
plt.xlabel('S')
plt.ylabel('P(S)')
plt.title('P(S/Genuine) and P(S/Imposter)')
plt.show()
plt.plot(listFPR,listTPR)
plt.xlabel('FPR Rate')
plt.ylabel('TPR Rate')
plt.title('ROC CURVE')
plt.show()
plt.plot(listFPR,listFNR)
plt.xlabel('FPR Rate')
plt.ylabel('FNR Rate')
plt.title('DET CURVE')
plt.show()
