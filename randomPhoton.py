import numpy as np
import math
import matplotlib.pyplot as plt

inFile = open("photonDistances2.dat", "r")

X = np.empty([])
Y = np.empty([])
Z = np.empty([])
R = np.empty([])
x_avg = 0
y_avg = 0
z_avg = 0
r_avg = 0
n = 1
sigma_x = 0
sigma_y = 0
sigma_z = 0
sigma_r = 0
for line in inFile:
    x, y, z, r = line.split()
    x = float(x); y = float(y); z = float(z); r = float(r)
    X = np.append(X, x)
    Y = np.append(Y, y)
    Z = np.append(Z, z)
    r = np.append(R, r)
    delta = x - x_avg
    x_avg += delta/n
    delta2 = x - x_avg
    sigma_x += delta*delta2
    delta = y - y_avg
    y_avg += delta/n
    delta2 = y - y_avg
    sigma_y += delta*delta2
    delta = z - z_avg
    z_avg += delta/n
    delta2 = z - z_avg
    sigma_z += delta*delta2
    delta = r - r_avg
    r_avg += delta/n
    delta2 = r - r_avg
    sigma_r = delta*delta2
    n += 1

print(X.mean(), "+/-", X.std())
print(Y.mean(), "+/-", Y.std())
print(Z.mean(), "+/-", Z.std())

plt.hist(X, bins = 'fd', density = True)
plt.savefig("Xhistogram.pdf")
plt.clf()
plt.hist(Y, bins = 'fd', density = True)
plt.savefig("Yhistogram.pdf")
plt.clf()
plt.hist(Z, bins = 'fd', density = True)
plt.savefig("Zhistogram.pdf")
plt.clf()