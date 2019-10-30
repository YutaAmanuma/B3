import random
import matplotlib.pyplot as plt

def transformation_1(x1,y1):
    x2 = 0.5*x1
    y2 = 0.5*y1
    return x2, y2

def transformation_2(x1,y1):
    x2 = 0.5*x1+0.5
    y2 = 0.5*y1+0.5
    return x2, y2

def transformation_3(x1,y1):
    x2 = 0.5*x1+1
    y2 = 0.5*y1
    return x2, y2



def transform(x1,y1):
     r = random.random()
     if r <= 0.333:
        x2, y2=transformation_1(x1, y1)
     elif 0.333 < r <= 0.666:
        x2, y2= transformation_2(x1, y1)
     else:
        x2, y2=transformation_3(x1, y1)
        
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
    n = int(input('Enter the number of points in the Sierpinski: '))
    x, y =draw_fern(n)
    plt.plot(x, y, 'o')
    plt.title('Sierpinski with {0} points'.format(n))
    plt.show()

