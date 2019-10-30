import matplotlib.pyplot as plt
def transformation_1(x1,y1):
    x2 = 0.85*x1 + 0.04*y1
    y2 = -0.04*x1 + 0.85*y1+1.6
    return x2, y2

def transformation_2(x1,y1):
    x2 = 0.2*x1-0.26*y1
    y2 = 0.23*x1 + 0.22*y1 + 1.6
    return x2, y2

def transformation_3(x1,y1):
    x2 = -0.15*x1 + 0.28*y1
    y2 = 0.26*x1 + 0.24*y1 + 0.44
    return x2, y2

def transformation_4(x1,y1):
    x2 = 0
    y2 = 0.16*y1
    return x2,y2

def logistic(x1,a):
    x2 = a*x1*(1-x1)
    return x2

def cycle(x0,N,a):
    n = [0]
    x = [x0]
    x1 = x0
    for i in range(N):
        x2 = logistic(x1,a)
        n.append(i)
        x.append(x2)
        x1 = x2
    return x

def transform(n,x0,a):
    x = [0]
    y = [0]

    x1, y1 = 0, 0

    r = cycle(x0,n,a)
    for i in r:
         if i <= 0.85:
             x2, y2=transformation_1(x1, y1)
         elif 0.85 < i <= 0.92:
             x2, y2= transformation_2(x1, y1)
         elif 0.92 < i <= 0.99:
             x2, y2=transformation_3(x1, y1)
         else:
             x2, y2=transformation_4(x1, y1)
         x.append(x2)
         y.append(y2)
         x1, y1 = x2, y2
    return x, y


if __name__=='__main__':
    n = int(input('Enter the number of points in the Fern: '))
    a = float(input('Decide the parameter: '))
    x0= float(input('Enter the first position: '))
    x, y=transform(n,x0,a)
    plt.plot(x, y, 'o')
    plt.title('Fern with {0} points'.format(n))
    plt.show()




