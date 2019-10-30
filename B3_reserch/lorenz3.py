import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def funcx(x,y,z):
    f = -10*x+10*y
    return f
def funcy(x,y,z):
    f = -x*z+28*x-y
    return f
def funcz(x,y,z):
    f = x*y-8/3*z
    return f
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
    y2 = y1+(t1+2*t2+2*t3+t4)*h/6
    z2 = z1+(u1+2*u2+2*u3+u4)*h/6

    return x2,y2,z2
def loop(n,x0,y0,z0,X0,Y0,Z0,h):
    N=[]
    r=[]

    for i in range(n):
        x1,y1,z1=kutta(x0,y0,z0,h)
        X1,Y1,Z1=kutta(X0,Y0,Z0,h)
        R=((X1-x0)**2+(Y1-y1)**2+(Z1-z1)**2)**0.5
        N.append(i*h)
        r.append(R)
        x0, y0, z0=x1, y1, z1
        X0,Y0,Z0=X1,Y1,Z1
    return r,N
if __name__=='__main__':
    
    x0= float(input('Enter the first positionx: '))
    y0= float(input('Enter the first positiony: '))
    z0= float(input('Enter the first positionz: '))
    X0= float(input('Enter the first positionx: '))
    Y0= float(input('Enter the first positiony: '))
    Z0= float(input('Enter the first positionz: '))
    n = int(input('Enter the number of calculations: '))
    h = float(input('Enter the bar range: '))
    r,n = loop(n,x0,y0,z0,X0,Y0,Z0,h)
    plt.plot(n,r)
    
    plt.show()
    
