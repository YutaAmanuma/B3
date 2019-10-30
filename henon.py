import matplotlib.pyplot as plt

def transform(x1,y1):
    x2=y1+1-1.4*x1**2
    y2=0.3*x1

    return x2,y2

def draw(n,x1,y1):
    x=[0]
    y=[0]

    for i in range(n):
        x1,y1=transform(x1,y1)
        x.append(x1)
        y.append(y1)
    return x,y

if __name__=='__main__':
    n = int(input('Enter the number of points in the Fern: '))
    x1, y1= 1,1
    x, y =draw(n,x1,y1)
    plt.plot(x, y, '.')
    plt.title('Henon with {0} points'.format(n))
    plt.show()
    
