# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import matplotlib as pl
from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import meshgrid
import numpy as np
import math
import random
# generate random floating point values
from random import seed


x1 = np.linspace(-5, 5, 1000)
x2 = np.linspace(-5, 5, 1000)


def f1(x1, x2):
    return (x1**2 + x2 - 11)**2+(x1+x2**2-7)**2

# r_min, r_max = -5.0, 5.0
# xaxis = arange(r_min, r_max, 0.1)
# yaxis = arange(r_min, r_max, 0.1)
# x, y = np.meshgrid(xaxis, yaxis)
# results = f1(x, y)
# figure = plt.figure()
# axis = plt.axes(projection='3d')
# axis.plot_surface(x, y, results, cmap='jet', shade= "false")
# axis.set_xlabel('x1')
# axis.set_ylabel('x2')
# axis.set_zlabel('z')
# plt.title('Funkcja Himmelblau\'a')
# plt.show()
# z=[]
# for i in range(1000):
#     z.append(int(i))
#
# fun = plt.contourf(x,y,results, [0,5,10,15,20,25,30,35,40,45,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,380,450,500,550,600,650,700,800], cmap='turbo')
# CB = plt.colorbar(fun, shrink=0.8, extend='both')
# plt.title('Funkcja Himmelblau\'a - wykres konturowy')
# plt.show()
#
#
# x3 = np.linspace(-35, 35, 1000)

def ackley(variables: np.array):
    sum1 = np.sum(variables ** 2)
    sum2 = np.sum(cos(2*pi*variables))
    return -20.0 * exp(-0.02 * sqrt(1/len(variables)) * sum1) - exp(1/len(variables) * sum2) + e + 20

def f2(x1, x2):
    return -20.0 * exp(-0.02 * sqrt(0.5 * (x1**2 + x2**2)))-exp(0.5 * (cos(2 * pi * x1)+cos(2 * pi * x2))) + e + 20

# r_min, r_max = -35.0, 35.0
# xaxis = arange(r_min, r_max, 2.0)
# yaxis = arange(r_min, r_max, 2.0)
# x, y = meshgrid(xaxis, yaxis)
# results = f2(x, y)
# figure = plt.figure()
# axis = plt.axes(projection='3d')
# axis.plot_surface(x, y, results, cmap='jet', shade= "false")
# axis.set_xlabel('x1')
# axis.set_ylabel('x2')
# axis.set_zlabel('f1(x1,x2)')
# plt.title('Funkcja Ackley\'a')
# plt.show()
# fun = plt.contourf(x,y,results, [0,1,2,3,4,5,6,7,8,9,10], cmap='turbo')
# CB = plt.colorbar(fun, shrink=0.8, extend='both')
# plt.title('Funkcja Ackley\'a - wykres konturowy')
# plt.show()

def randomSearch(i,myFunction,bound_max, bound_min):
    x = random.random()
    y = random.random()
    new_x = -5 + (x * (5-(-5)))
    new_y = -5 + (y * (5-(-5)))
    min_x = new_x
    min_y = new_y
    min_f = f1(new_x,new_y)
    for k in range(1,i):
        x = random.random()
        y = random.random()
        new_x = bound_min + (x * (bound_max - (bound_min)))
        new_y = bound_min + (y * (bound_max - (bound_min)))
        if myFunction(new_x, new_y) < min_f:
            min_f = myFunction(new_x, new_y)
            min_x = new_x
            min_y = new_y
    print("Znalezione minimum dla i = ",i,": w punkcie ",min_x, min_y, "wynosi ", min_f)


print('Funkcja Himmelblau\'a, algorytm RandomSearch: ')
randomSearch(500000, f1, -5,5)

print('Funkcja Ackley\'a, algorytm RandomSearch: ')
randomSearch(1000000, f2, -35,35)


print('\n\nWartosc funkcji f1 w punkcie (3,2):    f1(3,2) = ', f1(3,2))

print('\nWartosc funkcji f2 w punkcie (0,0):    f2(0,0) = ', ackley(np.array([0,0])))
