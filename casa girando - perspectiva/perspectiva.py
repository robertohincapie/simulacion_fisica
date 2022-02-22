# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 09:45:33 2021

@author: UPB
"""
import numpy as np
import matplotlib.pyplot as plt

#Objeto a dibujar
lineas=[]
lineas.append([(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,0)])
lineas.append([(0,0,1),(1,0,1),(1,1,1),(0,1,1),(0,0,1)])
lineas.append([(0,0,0),(0,0,1)])
lineas.append([(1,0,0),(1,0,1)])
lineas.append([(0,1,0),(0,1,1)])
lineas.append([(1,1,0),(1,1,1)])
lineas.append([(0,0,1),(0,0.5,1.5),(0,1,1)])
lineas.append([(1,0,1),(1,0.5,1.5),(1,1,1)])
lineas.append([(0,0.5,1.5),(1,0.5,1.5)])
lineas.append([(0,0.25,0.25),(0,0.25,0.75),(0,0.75,0.75),(0,0.75,0.25),(0,0.25,0.25)])

def dibujar(theta=60*np.pi/180, fi=0*np.pi/180, d=5, lineas=[], color='-k'):
    mu=np.array([np.cos(theta)*np.cos(fi), np.sin(theta)*np.cos(fi), np.sin(fi)])
    i=np.array([-np.sin(theta), np.cos(theta),0])
    j=np.cross(mu,i)
    for item in lineas:
        for k in range(1,len(item)):
            x1,y1,z1=item[k-1]
            x2,y2,z2=item[k]
            r1=np.array([x1,y1,z1-0.5])
            t1=d/(d-np.dot(mu,r1))
            xp1, yp1=t1*np.dot(r1,i),t1*np.dot(r1,j)
            r2=np.array([x2,y2,z2-0.5])
            t2=d/(d-np.dot(mu,r2))
            xp2, yp2=t2*np.dot(r2,i),t2*np.dot(r2,j)
            plt.plot([xp1,xp2],[yp1,yp2],color)
            A=np.array([xp2-xp1, yp2-yp1])
            Ro=np.array([(xp2+xp1)/2, (yp2+yp1)/2])
            a,b=Ro-10*A,Ro+10*A
            #plt.plot([a[0],b[0]],[a[1],b[1]],':c')
    plt.axis('equal')    

plt.close('all')
plt.figure(figsize=(5.89, 1.93))
    
for theta in np.arange(0,5000,3):
    fi=np.cos(2*np.pi*theta/730)*20+20
    d=5
    plt.subplot(1,2,1)
    plt.cla()
    dibujar(theta*np.pi/180, fi=fi*np.pi/180, d=d, lineas=lineas, color='-k')
    plt.subplot(1,2,2)
    plt.cla()
    dibujar((theta+5)*np.pi/180, fi=fi*np.pi/180, d=d, lineas=lineas, color='-k')
    plt.pause(0.001)        