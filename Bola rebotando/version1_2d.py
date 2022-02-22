# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:41:10 2021

@author: 000010478
"""
import numpy as np
import matplotlib.pyplot as plt

x=0
vx=0
y=1
vy=0
theta=0
w=-4
R=1
K=2/5
g=9.8
m=2
ex=0
ey=.99
dt=0.001
plt.close('all')
plt.figure(figsize=(4.78,6.4))
ax=plt.subplot(1,1,1)
def dibujar(x,y,R,theta,xmin=-5, xmax=5, ymin=-1, ymax=9):
    ax.clear()
    co=['or','ob','og','om']
    ang=np.linspace(0,2*np.pi,100)
    xc=np.cos(ang)*R+x
    yc=np.sin(ang)*R+y
    plt.plot(xc,yc,'-k')
    for da,color in zip(np.array([0,1,2,3])*np.pi/2, co):
        xc=np.cos(theta+da)*R+x
        yc=np.sin(theta+da)*R+y
        plt.plot(xc,yc,color)
    plt.axis('equal')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.grid()
    plt.pause(0.01)
def rebotar(vx,vy,w):
    print('Antes: uo=',vx,'wo=',w)
    #wf=vx/R*(1-ex)/(1-K)-w*(K-ex)/(1-K)
    #vfy=-ey*vy
    #vfx=vx+K*R*(wf-w)
    
    #wf=(-K*w+vx/R)/(K-1)
    vfy=-ey*vy
    #vfx=-wf*R
    #vfx=(vx-K*R*w)/(K+1)
    #wf=-vfx/R
    
    vfx=vx*(1-K*ex)/(1+K)-K*R*w*(1+ex)/(1+K)
    wf=w+(vfx-vx)/(K*R)
    print('Despues: uf=',vfx,'wf=',wf)
    return vfx, vfy, wf, R

def mover(x,vx,y,vy,theta,w,dt):
    if(y-R<0):
        vx,vy,w,y=rebotar(vx,vy,w)
    x=x+vx*dt
    vy=vy-g*dt
    y=y+vy*dt
    theta=theta+w*dt
        
    return x,vx,y,vy,theta,w

for i in range(10000):
    x,vx,y,vy,theta,w=mover(x,vx,y,vy,theta,w,dt)
    if(i%20==0):
        dibujar(x,y,R,theta)
