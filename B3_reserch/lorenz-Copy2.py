
# coding: utf-8

# In[47]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats as st
import scipy.fftpack
import prettyplotlib as ppl
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import*
get_ipython().magic('matplotlib inline')


# In[2]:


def funcx(x,y,z):
    return -10*x+10*y
def funcy(x,y,z):
    return -x*z+15*x-y
def funcz(x,y,z):
    return x*y-8/3*z


# In[3]:


def kutta(x1,y1,z1,h):
    s1 = funcx(x1,y1,z1)
    t1 = funcy(x1,y1,z1)
    u1 = funcz(x1,y1,z1)
    
    s2 = funcx(x1+h*s1/2,y1+h*t1/2,z1+h*u1/2)
    t2 = funcy(x1+h*s1/2,y1+h*t1/2,z1+h*u1/2)
    u2 = funcz(x1+h*s1/2,y1+h*t1/2,z1+h*u1/2)
    
    s3 = funcx(x1+h*s2/2,y1+h*t2/2,z1+h*u2/2)
    t3 = funcy(x1+h*s2/2,y1+h*t2/2,z1+h*u2/2)
    u3 = funcz(x1+h*s2/2,y1+h*t2/2,z1+h*u2/2)
    
    s4 = funcx(x1+h*s3,y1+h*t3,z1+h*u3)
    t4 = funcy(x1+h*s3,y1+h*t3,z1+h*u3)
    u4 = funcz(x1+h*s3,y1+h*t3,z1+h*u3)
    
    x2 = x1+(s1+2*s2+2*s3+s4)*h/6
    y2 = y1+(t1+2*t2+2*t2+t4)*h/6
    z2 = z1+(u1+2*u2+2*u3+u4)*h/6
    
    return x2, y2, z2


# In[12]:


def loop(x0,y0,z0,h):
    for i in range(1000):
        x1,y1,z1=kutta(x0,y0,z0,h)
        x0,y0,z0=x1,y1,z1
    if x1>0:
        return 1
    else:
        return 0


# In[49]:


def distribution():
    x1=[]
    y1=[]
    z1=[]
    x2=[]
    y2=[]
    z2=[]
    for i in range(40):
        x0=-50+i*2.5
        for j in range(40):
            y0=-50+j*2.5
            for k in range(25):
                z0=-50+k*2.5
                l=loop(x0,y0,z0,0.01)
                if l==1:
                    x1.append(x0)
                    y1.append(y0)
                    z1.append(z0)
                else:
                    x2.append(x0)
                    y2.append(y0)
                    z2.append(z0)
    x1=np.array(x1)
    y1=np.array(y1)
    z1=np.array(z1)
    x2=np.array(x2)
    y2=np.array(y2)
    z2=np.array(z2)
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot(x1,y1,z1,".",ms=1.3)
    ax.plot(x2,y2,z2,".",ms=1.3)
    return x1,y1,z1,x2,y2,z2


if __name__=='__main__':
    x1,y1,z1,x2,y2,z2=distribution()

