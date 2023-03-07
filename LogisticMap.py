# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:38:43 2023

@author: ken3

Introduction:
    The logistic map is a mathematical model that describes the population growth 
    in a limited environment. It is a recurrence equation that 
    is defined by the following formula:
        x(n+1) = r * x(n) * (1 - x(n))
    The logistic map is a simple yet powerful model that exhibits complex behavior such as bifurcation and chaos as the value of r increases.

Reference:
    https://en.wikipedia.org/wiki/Logistic_map

"""

import numpy as np
import matplotlib.pyplot as plt

interval = (2.8, 4)  # start, end
accuracy = 0.0001
reps = 600  # number of repetitions
numtoplot = 200
lims = np.zeros(reps)

fig, biax = plt.subplots()
fig.set_size_inches(16, 9)

lims[0] = np.random.rand()
for r in np.arange(interval[0], interval[1], accuracy):
    for i in range(reps-1):
        lims[i+1] = r*lims[i]*(1-lims[i])

    biax.plot([r]*numtoplot, lims[reps-numtoplot:], 'b.', markersize=.02)

biax.set(xlabel='r', ylabel='x', title='logistic map')
plt.show()