# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 22:27:08 2023

@author: Ken3

Introduction
    Firstly, a system is considered linear if it satisfies the principle of 
    superposition, which means that the response of the system to the sum of 
    two input signals is equal to the sum of the individual responses to 
    each input signal.

    Secondly, a system is considered time-invariant if its behavior 
    does not change with respect to time, meaning that its response to 
    an input signal remains the same regardless of when the input signal is applied.
    
    The behavior of an LTI system is typically described mathematically 
    using a differential equation or a difference equation, which relates 
    the input and output signals. The Laplace transform and the Z-transform 
    are commonly used to analyze LTI systems in the continuous-time and 
    discrete-time domains, respectively.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer function of the LTI system
num = [1, 2, 1]   # Numerator polynomial
den = [1, 4, 3]   # Denominator polynomial
sys = signal.lti(num, den)

# Generate the input signal
t = np.linspace(0, 10, 1000)   # Time vector
u = np.sin(t) + np.cos(2*t)    # Input signal

# Calculate the response of the LTI system to the input signal
t, y, _ = signal.lsim(sys, u, t)

# Plot the input and output signals
plt.plot(t, u, label='Input')
plt.plot(t, y, label='Output')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Signal')
plt.show()