import numpy as np
import math
import random


def step(pos, N, mu, sigma):
    dx = np.random.normal(mu, sigma, N)
    dy = np.random.normal(mu, sigma, N)
    dz = np.random.normal(mu, sigma, N)
    pos[0] += np.sum(dx)
    pos[1] += np.sum(dy)
    pos[2] += np.sum(dz)
    return pos

pos = [0.0, 0.0, 0.0]
pos = step(pos, 100000000, 0.0, 57.735)
print(pos[0], ", ", pos[1], ", ", pos[2])

    
    #s = np.random.normal(.01, .00577 , 1000)
    #phi = np.random.uniform(0, 2*np.pi, 1000)   
    #x = s*np.cos(phi)*np.sin(theta)
    #y = s*np.sin(phi)*np.sin(theta)
    #z = s*np.cos(theta)
    #return x, y, z

#mu = .01 #m
#sigma = .00577 #m

#for i in range(0, N):
    #x[i], y[i], z[i] = step()


#avg = (X+Y+Z)/1000
#std_x = np.std(x)
#std_y = np.std(y)
#std_z = np.std(z)

#RMS = N*avg**2 + N*(N-1)*avg**2