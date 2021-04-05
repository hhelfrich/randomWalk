import numpy as np
import math
import random
import matplotlib.pyplot as plt

dx = normal(0.0, 3241363943, 10000000)
dy = normal(0.0, 3241363943, 10000000)
dz = normal(0.0, 3241363943, 10000000)
x = 0, y = 0, z = 0, r = 0, i = 0
while (r < 636.94E6):
    x += dx[i]
    y += dy[i]
    z += dz[i]
    r = SQRT(x**2 + y**2 + z**2)
    i += 1

print(i)

#t = i in years

