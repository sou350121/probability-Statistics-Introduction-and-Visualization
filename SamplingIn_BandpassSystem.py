# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:19:47 2023

@author: ken3

Introduction:
    Consider a continuous-time signal xc(t) = Sa (4πt) cos (12πt)
    1. Illustrate |Xc (jΩ)|;
    2. Verify that the Nyguist rate is T= 1/16, though lower rate T′= 1/8 also does not produce aliasing;
"""

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the continuous-time signal
t = sp.symbols('t')
xc = sp.sinc(4*sp.pi*t)*sp.cos(12*sp.pi*t)

# Compute the Fourier transform of xc
w = sp.symbols('w')
Xc = sp.fourier_transform(xc, t, w)

# Plot the magnitude of Xc
sp.plotting.plot(sp.re(Xc), (w, -20*sp.pi, 20*sp.pi), xlabel='w (rad/s)', ylabel='|Xc(jw)|', title='Magnitude of Fourier Transform of xc')

# Verify the Nyquist rate
T = 1/16
T_prime = 1/8
w_max = sp.pi/T
w_prime_max = sp.pi/T_prime
Xc_max = abs(Xc.subs(w, w_max))
Xc_prime_max = abs(Xc.subs(w, w_prime_max))
if Xc_max == 0:
    print('Nyquist rate is', T)
elif Xc_prime_max == 0:
    print('Nyquist rate is', T_prime)
else:
    print('Nyquist rate is between', T, 'and', T_prime)

# Visualize xc
t_vals = np.linspace(-1, 1, 1000)
xc_vals = np.array([xc.subs(t, t_val) for t_val in t_vals])
plt.plot(t_vals, xc_vals)
plt.xlabel('t')
plt.ylabel('xc(t)')
plt.show()
