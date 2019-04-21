import numpy as np
import matplotlib.pyplot as plt
listn=[]
listn1=[]
listn2=[]
x=0
for i in range(10000):
	x+=0.1
	y=np.exp(-(x-20)**2 / (2*5))/(np.sqrt(2*np.pi*5))
	y1=np.exp(-(x-60)**2 / (2*15))/(np.sqrt(2*np.pi*15))
	listn.append(x)
	listn1.append(y)
	listn2.append(y1)
plt.plot(listn,listn1)
plt.plot(listn,listn2)
plt.show()
