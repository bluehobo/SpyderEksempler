# -*- coding: utf-8 -*-
"""
Numerisk integrasjon

Created on Tue Sep 28 14:40:32 2021

@author: sir
"""
# Importerer nødvendige biblioteker
import numpy as np
# import math as math
import matplotlib.pyplot as plt

# Definerer funksjoner
def fn(x):
    return x**3

def Fn(x):
    return (1/4)*x**4

# Parametere for Riemmannsum
a = 2
b = 4
dx = 1e-3

N = int((b-a)/dx + 1) # +1 fordi jeg vil ha med endepunktet i plottet

# Setter opp xverdiene
x = np.linspace(a, b, N)

#print(x)

# Plotter funksjonen
plt.plot(x,fn(x))

# Summerer rektanglene under grafen
minSum=0.0
for i in range(x.size - 1): # -1 fordi vi ser på arealet fra og med a TIL b, ikke til og med)
    minSum = minSum + fn(x[i])*dx #Riemannsum!
    #print(minSum) for debug

analytisk = Fn(b) - Fn(a)

print("riemannsum:", round(minSum, 3))
print("analytisk:", analytisk)
print("differanse:", analytisk - minSum)