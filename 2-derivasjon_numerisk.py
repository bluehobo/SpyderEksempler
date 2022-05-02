# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:59:57 2021

@author: sir
"""

x_verdi=2
dx=1e-8


def f(x):
    return x**3 - 2*x**2 + 2*x - 5

def numerisk_derivert(f, x, delta_x):
    fder = (f(x + delta_x)-f(x))/delta_x
    return fder

numder = numerisk_derivert(f, x_verdi, dx)

print("f'(",x_verdi,")=", numder)