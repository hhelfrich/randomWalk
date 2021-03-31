import numpy as np
import math
import random

def step():
    s = np.random.normal(.01, .00577 , 1000)
    theta = np.random.uniform(0, np.pi, 1000)
    phi = np.random.uniform(0, 2*np.pi, 1000)   
    x = s*np.cos(phi)*np.sin(theta)
    y = s*np.sin(phi)*np.sin(theta)
    z = s*np.cos(theta)
    return x, y, z

#mu = .01 #m
#sigma = .00577 #m

#for i in range(0, N):
    #x[i], y[i], z[i] = step()

x = np.zeros(1000)
y = np.zeros(1000)
z = np.zeros(1000)

x, y, z = step()

X = np.sum([x])
Y = np.sum([y])
Z = np.sum([z])

print(X + Y + Z)
