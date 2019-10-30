import matplotlib.pyplot as plt
import prettyplotlib as ppl
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
    return n,x

if __name__=='__main__':
    x0=0.0001
    n1, x1 = cycle(x0,1000,2.8)
    n2, x2 = cycle(x0,1000,3.1)
    n3, x3 = cycle(x0,1000,3.5)
    n5, x5 = cycle(x0,1000,3.83)
    n4, x4 = cycle(x0,1000,4)
    
    ppl.plot(n4,x4,label="r=4") 
    plt.legend()
    plt.ylim(0,1)
    plt.xlim(930,1000)
    plt.title('Logistic map')
    plt.show()
    
    
