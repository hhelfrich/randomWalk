import numpy as np
import math
import random
import matplotlib.pyplot as plt

dx = np.random.normal(0.0, 324136.3943, 10000000)
dy = np.random.normal(0.0, 324136.3943, 10000000)
dz = np.random.normal(0.0, 324136.3943, 10000000)
x = 0
y = 0
z = 0
r = 0
i = 0
while (r < 695700000):
    x += dx[i]
    y += dy[i]
    z += dz[i]
    r = np.sqrt(x**2 + y**2 + z**2)
    i += 1

t = i # in years
print(t)

