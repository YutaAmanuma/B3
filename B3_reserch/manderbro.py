import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def initialize_image(x_p,y_p):
    image=[]
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def color_points(max_iteration):
    x_p=4000
    y_p=4000
    image = initialize_image(x_p,y_p)
    for i in range(y_p):
        for j in range(x_p):
            iteration=0
            z1=complex(0,0)
            c=complex(3.5/x_p*j-2.5,2/y_p*i-1)
            z1=z1**2+c
            iteration=iteration+1
            while (abs(z1)<2 and iteration<max_iteration):
                z1=z1**2+c
                iteration=iteration+1
            image[i][j]=iteration
    plt.imshow(image, extent=(-2.5,1,-1,1))
    plt.show()

if __name__=='__main__':
    max_iteration=int(input('Enter max_interation: '))
    color_points(max_iteration)     
                
                
            
