
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats as st
import scipy.fftpack
import prettyplotlib as ppl
from mpl_toolkits.mplot3d import Axes3D
get_ipython().magic('matplotlib inline')


# In[2]:


def funcx(x,y,z):
    return -10*x+10*y
def funcy(x,y,z):
    return -x*z+28*x-y
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


# In[18]:


def loop(n,x0,y0,z0,h):
    x=[x0]
    y=[y0]
    z=[z0]
    T=[0]
    j=[0]
    N=[0]
    Z1=[]
    Z2=[]
    x1,y1,z1=kutta(x0,y0,z0,h)
    x2,y2,z2=kutta(x1,y1,z1,h)
    for i in range(n):
        x0,y0,z0=kutta(x0,y0,z0,h)
        x1,y1,z1=kutta(x1,y1,z1,h)
        x2,y2,z2=kutta(x2,y2,z2,h)
        x.append(x0)
        y.append(y0)
        z.append(z0)
        T.append(i*h)
        if z0<z1 and z2<z1:
            Z1.append(z1)
            Z2.append(z1)
    return x,y,z,T,j,N,Z1,Z2


# In[37]:


x,y,z,t,j,N,Z1,Z2 = loop(100000,10,10,10,0.001)
x = np.array(x)
y = np.array(y)
z = np.array(z)
t = np.array(t)
j = np.array(j)
N = np.array(N)
Z1= np.array(Z1)
Z2= np.array(Z2)


# In[33]:


x1=np.linspace(0,50,2)
y1=x1
y2=77.25-x1


# In[34]:


ppl.plot(Z2,Z1,".",ms=1)
ppl.plot(x1,y1)
ppl.plot(x1,y2)
plt.xlim(25,50)
plt.ylim(30,50)


# In[38]:


ppl.plot(t,x)
print(x)

t_ = np.array([0,100])
y_ = np.array([0,0])
ppl.plot(t_, y_)
plt.xlabel('time(s)')


# In[74]:


ppl.plot(t,z)
plt.xlabel('time(s)')
plt.xlim(0,3)


# In[44]:


ppl.plot(x,z)


# In[57]:


df_xy = pd.DataFrame({'x':x,'y':y})
df_xy.tail()


# In[58]:


df_xy.corr()


# In[59]:


df_xy['y']= df_xy['y']>df_xy['y'].median()
df_xy['x']= df_xy['x']>df_xy['x'].median()


# In[61]:


st.chi2_contingency(_)


# In[60]:


pd.crosstab(df_xy['x'],df_xy['y'])


# In[77]:


x_fft = sp.fftpack.fft(x)


# In[78]:


z_fft = sp.fftpack.fft(z)


# In[79]:


x_psd = np.abs(x_fft)**2


# In[80]:


z_psd = np.abs(z_fft)**2


# In[81]:


fftfreq = sp.fftpack.fftfreq(len(x_psd),1./1000)


# In[82]:


fftfreq = sp.fftpack.fftfreq(len(z_psd),1./1000)


# In[83]:


i = fftfreq > 0


# In[84]:


ppl.plot(fftfreq[i], 10*np.log(x_psd[i]))
plt.xlabel('Frequency(1/s)')
plt.ylabel('x')


# In[85]:


ppl.plot(fftfreq[i], 10*np.log(z_psd[i]))
plt.xlabel('Frequency(1/s)')
plt.ylabel('z')


# In[86]:


ppl.plot(fftfreq[i], 10*np.log(x_psd[i]))
plt.xlim(0,10)
plt.xlabel('Frequency(1/s)')
plt.ylabel('x')


# In[88]:


ppl.plot(fftfreq[i], 10*np.log(z_psd[i]))
plt.xlim(1,2)
plt.xlabel('Frequency(1/s)')
plt.ylabel('z')


# In[8]:


def autocorr(x):
    result = np.correlate(x,x, mode='full')
    return result[result.size//2:]


# In[9]:


def autocorr_lorenz(x,variable):
    z=autocorr(x)
    plt.subplot(122)
    ppl.plot(t,z/float(z.max()),'-',label= variable)
    plt.xlabel('time(s)')
    plt.legend()
    plt.title('Autocorelation')


# In[19]:


autocorr_lorenz(x,'x')
autocorr_lorenz(y,'y')
autocorr_lorenz(z,'z')


# In[20]:


autocorr_lorenz(x,'x')


# In[21]:


autocorr_lorenz(z,'z')


# In[12]:


fig= plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z)


# In[68]:


fig= plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z)


# In[18]:


fig= plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z)


# In[39]:


ppl.plot(x,y)


# In[51]:


ppl.plot(x,y)


# In[13]:


ppl.plot(t,j)


# In[10]:


autocorr_lorenz(j,'jump')


# In[23]:


jump_fft = sp.fftpack.fft(j)


# In[24]:


j_psd = np.abs(jump_fft)**2


# In[28]:


fftfreq2 = sp.fftpack.fftfreq(len(j_psd),1./10000)


# In[29]:


i=fftfreq>0


# In[31]:


ppl.plot(fftfreq2[i], 10*np.log10(j_psd[i]))
plt.xlabel('Frequency(1/s)')
plt.ylabel('jump')


# In[33]:


ppl.plot(fftfreq2[i], 10*np.log10(j_psd[i]))
plt.xlim(0,10)
plt.ylim(-10,30)
plt.xlabel('Frequency(1/s)')
plt.ylabel('jump')


# In[14]:


ppl.plot(t,N)
plt.xlim(0,20)
plt.ylim(0,15)

