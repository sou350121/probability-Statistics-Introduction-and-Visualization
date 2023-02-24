# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:18:10 2023

@author: ken3

Introduction:
    Fourier series is a mathematical tool used to represent a periodic function
    as a sum of sine and cosine functions of different frequencies. 
    This representation allows us to analyze the frequency content of the periodic signal.
"""

import numpy as np

# Define the periodic square wave function
def square_wave(t, T):
    return np.where(np.mod(t, T) < T/2, 1, -1)

# Define the Fourier series coefficients
def fourier_coefficients(f, T, n):
    a0 = 1/T * np.trapz(f(t, T), t)
    an = np.zeros(n+1)
    bn = np.zeros(n+1)
    for i in range(1, n+1):
        # np.traz- Integrate along the given axis using the composite trapezoidal rule.
        an[i] = 2/T * np.trapz(f(t, T) * np.cos(2*np.pi*i*t/T), t)  
        bn[i] = 2/T * np.trapz(f(t, T) * np.sin(2*np.pi*i*t/T), t)
    return a0, an, bn

# Compute the Fourier series coefficients for a periodic square wave
t = np.linspace(0, 10, num=1000)
T = 2
n = 10
a0, an, bn = fourier_coefficients(square_wave, T, n)

# Compute the Fourier series approximation
approx = a0/2
for i in range(1, n+1):
    approx += an[i] * np.cos(2*np.pi*i*t/T) + bn[i] * np.sin(2*np.pi*i*t/T)

# Plot the original square wave and its Fourier series approximation
import matplotlib.pyplot as plt
plt.plot(t, square_wave(t, T), label='Square wave')
plt.plot(t, approx, label='Fourier series')
plt.legend()
plt.show()