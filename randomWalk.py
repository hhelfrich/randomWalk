import numpy as np
import math
import random
import matplotlib.pyplot as plt

def step(pos, N, mu, sigma):
    dx = np.random.normal(mu, sigma, N)
    dy = np.random.normal(mu, sigma, N)
    dz = np.random.normal(mu, sigma, N)
    pos[0] += np.sum(dx)
    pos[1] += np.sum(dy)
    pos[2] += np.sum(dz)
    return pos

pos = [0.0, 0.0, 0.0]
pos = step(pos, 500000000, 0.0, 3241363943)
print(pos[0], ", ", pos[1], ", ", pos[2])

plt.hist(pos[0], bins = 'fd', density = True)
plt.savefig("Xhistogramyear.pdf")
plt.clf()
plt.hist(pos[1], bins = 'fd', density = True)
plt.savefig("Yhistogramyear.pdf")
plt.clf()
plt.hist(pos[2], bins = 'fd', density = True)
plt.savefig("Zhistogramyear.pdf")
plt.clf()

#sigman = SQRT(N)*sigma