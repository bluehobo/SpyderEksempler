# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:43:36 2021

@author: sir
"""

def f(x):
    return x**2 - 2

# analytisk derivert
def analytisk_derivert(x):
    return 2*x

def numerisk_derivert(f, x, delta_x):
    fder = (f(x + delta_x)-f(x))/delta_x
    return fder

delta_x = []

for i in range(1,16):
    dx = 10**(-i)
    delta_x.append(dx)
    numder = numerisk_derivert(f, 1, dx)
    ander = analytisk_derivert(1)
    feil = ander - numder
    print("Delta_x =", dx, " avvik:", feil)
    
# rare verdier for dx < 1e-8: har med presisjonen på hvordan en datamaskin lagrer tall