# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:20:59 2019

@author: HOME
"""

matrix=[[0,0,1,0,0],[0,0,1,1,0],[0,1,1,1,0],[0,1,1,0,0],[0,0,1,0,0]]
mom=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
central_mom=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


for i in matrix:
    print(i)


 
def moment(p,q,matrix): 
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            mom[q][p]=mom[q][p]+((x**p)*(y**q)*matrix[y][x])



def central_moment(p,q,matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            central_mom[q][p]=central_mom[q][p]+(((x-Cx)**p)*((y-Cy)**q)*matrix[y][x])
            
            


for p in range(len(matrix)):
    for q in range(len(matrix[0])):
        moment(p,q,matrix)
        
        
print("Area={}".format(mom[0][0]))
#print(mom[0][0])

Cx=mom[1][0]/mom[0][0]
Cy=mom[0][1]/mom[0][0]
print("Centroid Cx={0} and Cy={1}".format(Cx,Cy))

        

print("Moment Matrix :")
for i in mom:
    print(i)
        

for p in range(len(matrix)):
    for q in range(len(matrix[0])):
        central_moment(p,q,matrix)

print("Central Moment Matrix :")
for i in central_mom:
    print(i)

    
    
