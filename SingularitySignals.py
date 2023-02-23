# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:53:14 2023

@author: ken3
"""

import numpy as np

def step(t):
    return np.where(t >= 0, 1, 0)

def impulse(t):
    return np.where(t == 0, np.inf, 0)

def ramp(t):
    return np.where(t >= 0, t, 0)

def impulse_doublet(t, epsilon):
    return impulse(t) - impulse(t - epsilon)

import matplotlib.pyplot as plt

t = np.linspace(-1, 1, 1000)

plt.plot(t, step(t), label='Step')
plt.plot(t, impulse(t), label='Impulse')
plt.plot(t, ramp(t), label='Ramp')
plt.plot(t, impulse_doublet(t, 0.1), label='Impulse Doublet')

plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()