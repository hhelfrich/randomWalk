import numpy as np
import math
import random
import matplotlib.pyplot as plt

def step(pos, mu, sigma, N):
    dx = np.random.normal(mu, sigma, N)
    dy = np.random.normal(mu, sigma, N)
    dz = np.random.normal(mu, sigma, N)
    pos[0] += np.sum(dx)
    pos[1] += np.sum(dy)
    pos[2] += np.sum(dz)
    return pos, dx, dy, dz
dx = np.empty([])
dy = np.empty([])
dz = np.empty([])
pos = [0.0, 0.0, 0.0]
pos = step(pos, 0.0, 324136.394, 10000000)

x = 0
y = 0
z = 0
r = 0
i = 0
while (r < 636.94E6):
    x += dx[i]
    y += dy[i]
    z += dz[i]
    r = SQRT(x**2 + y**2 + z**2)
    i += 1

print(pos[0], ", ", pos[1], ", ", pos[2])
print(i)

#sigman = SQRT(N)*sigma