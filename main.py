# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5, 5, 1000)
x2 = np.linspace(-5, 5, 1000)


def f(x1, x2):
    return (x1**2 + x2 - 11)**2+(x1+x2**2-7)**2

X, Y = np.meshgrid(x1, x2)
Z = f(X, Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1,x2)');
plt.show()
