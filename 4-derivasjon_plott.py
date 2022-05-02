# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:34:08 2021

@author: sir
"""
import matplotlib.pyplot as plt
import numpy as np

dx=1e-8
x_min=0
x_maks=6.28
N=1000

# funksjonen som skal deriveres
def f(x):
    return np.sin(x)

# metode for numerisk derivasjon
def numerisk_derivert(f, x, delta_x):
    fder = (f(x + delta_x)-f(x))/delta_x
    return fder

# plotting
x = np.linspace(x_min, x_maks, N)
y = f(x)

yder = numerisk_derivert(f,x,dx)

plt.plot(x, y, color='green', label='f(x)')
plt.plot(x, yder, color='red', label='f\'(x)')

plt.xlabel('x')
plt.legend()
plt.grid()
plt.show()

