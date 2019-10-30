#円の領域推定
import matplotlib.pyplot as plt
import random
def calculate():
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2+y**2<=1:
        return 1,x,y
    else:
        return 0,x,y

def draw_gragh():
    circle = plt.Circle((0,0),radius = 1)

    return circle
             
    

def estimate(n):
    N=[0]
    x=[0]
    y=[0]
    for i in range(n):
        n1,x1,y1 = calculate()
        N.append(n1)
        x.append(x1)
        y.append(y1)

    f=4*sum(N)/n
    return f,x,y


if __name__=='__main__':
    n = int(input('Enter the number of calculation: '))
    f,x,y=estimate(n)
    print(f)
    c=draw_gragh()
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.add_patch(c)
    plt.axis([-1,1,-1,1])
    plt.plot(x,y,'o',c="g")
    plt.show()

        
