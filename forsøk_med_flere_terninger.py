# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:53:24 2022

@author: sigur
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# setter opp terning og antall kast. Endre på disse parameterene!
sider = 6
antall_terninger = 2
antall_forsok = 100

antall_mulige_utfall = antall_terninger * sider - (antall_terninger-1)
print(antall_mulige_utfall)
fordeling = np.zeros(antall_mulige_utfall)

# kaster terningen, husker sum og antall forekomster
for i in range (antall_forsok):
    sum=0
    
    for j in range(antall_terninger):
        sum += random.randint(1, sider)
    
    fordeling[sum-antall_terninger]+=1

# Lager et søylediagram over relativ frekvens, sannsynlighet for utfall
# angitt med rød linje, gjennomsnitt og forventningsverdi som vertikale linjer

relativ_frekvens = fordeling/antall_forsok
akse = np.linspace(0, antall_mulige_utfall, antall_mulige_utfall)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(akse,relativ_frekvens)
plt.show()