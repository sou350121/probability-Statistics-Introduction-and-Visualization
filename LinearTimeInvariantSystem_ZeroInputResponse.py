# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 09:57:13 2023

@author: ken3

Introduction:
    In this example, we define an LTI system with 
    transfer function H(s) = (s^2 + 2s + 1) / (s^2 - 0.5s + 0.25). 
    We then use the impulse function to compute the impulse response of the system, 
    which we then convolve with the initial conditions (x0 = 1, x1 = 2) to 
    obtain the zero-input response. 
"""

import numpy as np
from scipy.signal import impulse

# Define the LTI system
num = [1, 2, 1]  # Numerator coefficients of transfer function
den = [1, -0.5, 0.25]  # Denominator coefficients of transfer function

# Compute the impulse response of the system
t, h = impulse((num, den))

# Define the initial conditions
x0 = 1
x1 = 2

# Compute the zero-input response by convolving the impulse response with the initial conditions
yzi = x0*h + x1*np.gradient(h, t[1]-t[0])

# Plot the zero-input response
import matplotlib.pyplot as plt
plt.plot(t, yzi)
plt.xlabel('Time')
plt.ylabel('Zero-input response')
plt.show()