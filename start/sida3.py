import random
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


def transform(x1,y1):
     r = random.random()
     if r <= 0.85:
        x2, y2=transformation_1(x1, y1)
     elif 0.85 < r <= 0.92:
        x2, y2= transformation_2(x1, y1)
     elif 0.92 < r <= 0.99:
        x2, y2=transformation_3(x1, y1)
     else:
        x2, y2=transformation_4(x1, y1)
        
     return x2,y2

def draw_fern(n):
    x = [0]
    y = [0]

    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform(x1, y1)
        x.append(x1)
        y.append(y1)
    return x, y

if __name__=='__main__':
    n = int(input('Enter the number of points in the Fern: '))
    x, y =draw_fern(n)
    plt.plot(x, y, 'o')
    plt.title('Fern with {0} points'.format(n))
    plt.show()

