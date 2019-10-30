import numpy as np
import matplotlib.pyplot as plt

def transform1(p):
    x, y = p[0], p[1]
    x1 = 0.85*x + 0.04*y
    y1 = -0.04*x + 0.85*y + 1.6
    return x1, y1

def transform2(p):
    x, y = p[0], p[1]
    x1 = 0.2*x - 0.26*y
    y1 = 0.23*x + 0.22*y + 1.6
    return x1, y1
    
def transform3(p):
    x, y = p[0], p[1]
    x1 = -0.15*x + 0.28*y
    y1 = 0.26*x + 0.24*y + 0.44
    return x1, y1

def transform4(p):
    y = p[1]
    x1 = 0
    y1 = 0.16*y
    return x1, y1    

def transform(p):
    transforms =[transform1, transform2, transform3, transform4]
    # 0～3の中から、85%, 7%, 7%, 1%の重みでインデックスを選ぶ
    index = np.random.choice([0, 1, 2, 3], p=probability)
    t = transforms[index]
    x, y = t(p)
    return x, y

def draw(n):
    x, y = [0], [0]    # ｘ、ｙはn個の要素を持つリストになる
    x1, y1 = 0, 0      # 現在の座標
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x, y

n = 1000  # 点の数
# 85%, 7%, 7%, 1%
probability = [0.85, 0.07, 0.07, 0.01] # 合計が1.00
x, y = draw(n)
plt.plot(x, y, "o", c="g", markeredgecolor="darkgreen")
plt.title("Fern with {} points".format(n))
plt.show()
