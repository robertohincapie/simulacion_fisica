# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:54:20 2019

@author: Roberto H
"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
N=50
dx=0.01
Lmax=N*dx/2

x,y=np.meshgrid(np.linspace(-Lmax,Lmax,N),np.linspace(-Lmax,Lmax,N), sparse=False, indexing='ij')
r=np.sqrt(np.power(x,2)+np.power(y,2))
z=0*x
for k in range(1250):
    i=np.random.randint(low=2, high=N-2)
    j=np.random.randint(low=2, high=N-2)
    z[i,j]=2
#z[r<0.05]=-1

D=0.03
dt=0.0001
for k in range(300):
    z2=z
    for i in range(1,N-1):
        for j in range(1,N-1):
            z2[i,j]=z[i,j]+dt*(D*(z[i+1,j]+z[i-1,j]+z[i,j+1]+z[i,j-1]-4*z[i,j])/dx/dx+z[i,j]*(1-z[i,j])*(z[i,j]-0.3))
    z=z2
    if(k%10==0):
        plt.imshow(z)
        plt.title(str(k))
        plt.pause(0.01)
        
plt.colorbar()