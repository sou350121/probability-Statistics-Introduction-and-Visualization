# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:27:15 2023

@author: ken3

Introduction:
    Show the following integral by python
    1. ∑_(k=0)^∞ (1/(3k + 1) - 1/(3k + 2)) = √(3)*π/9
    2. ∫_(-∞)^∞ (sin(x)/x) dx
    3. x(t) = t, −π < t ≤ π with period x(t) = x(t + 2π). Determine its Fourier Series 
    
    
    
"""

# example 1
import math

result = 0
k = 0

while True:
    term = 1/(3*k + 1) - 1/(3*k + 2)
    if abs(term) < 1e-9:  # set tolerance for convergence
        break
    result += term
    k += 1

expected = math.sqrt(3) * math.pi / 9

print(f"Result: {result:.9f}")
print(f"Expected: {expected:.9f}")


# example 2
import scipy.integrate as spi
import numpy as np

# The lambda function passed to quad defines the integrand as sin(x)/x.

result, _ = spi.quad(lambda x: np.sin(x)/x, -np.inf, np.inf)

print(f"Result: {result:.9f}")

# example 3 
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Define symbols and period
x = sp.Symbol('x')
n = sp.Symbol('n')
T = 2*sp.pi

# Define function
f = x

# Calculate Fourier coefficients
a0 = sp.integrate(f, (x, -sp.pi, sp.pi)) / sp.pi
an = sp.integrate(f*sp.cos(n*x), (x, -sp.pi, sp.pi)) / sp.pi
bn = sp.integrate(f*sp.sin(n*x), (x, -sp.pi, sp.pi)) / sp.pi

# Define number of harmonics to include
num_harmonics = 10

# Calculate Fourier Series
fs = a0
for i in range(1, num_harmonics+1):
    fs += an.subs(n, i) * sp.cos(i*x) + bn.subs(n, i) * sp.sin(i*x)

# Plot function and Fourier Series
x_vals = np.linspace(-np.pi, np.pi, 1000)
f_vals = np.array([f.subs(x, xv) for xv in x_vals], dtype=np.float)
fs_vals = np.array([fs.subs(x, xv) for xv in x_vals], dtype=np.float)
plt.plot(x_vals, f_vals, label='Function')
plt.plot(x_vals, fs_vals, label='Fourier Series')
plt.legend()
plt.show()