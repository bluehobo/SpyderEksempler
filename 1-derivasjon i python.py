# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:05:05 2021

@author: sir
"""
# Dårlig kode. 2-4 for bedre kode.

import pylab as py

start = -3
stopp = 3
N = 100

def f(x):
    return  x**2

x = py.linspace(start,stopp,N)
py.plot(x, f(x))

derivert = py.zeros(N) # lager en tom Array like stor som x

for i in range(N-1):
    derivert[i] = (f(x[i+1])-f(x[i]))/(x[i+1]-x[i])
    
py.plot(x[:N-1],derivert[:N-1])
    


