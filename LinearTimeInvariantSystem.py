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
sys = signal.lti(num, den)  # an instance of the LTI class or a tuple describing the system.

# Generate the input signal
t = np.linspace(0, 10, 1000)   # Time vector
u = np.sin(t) + np.cos(2*t)    # Input signal

# Calculate the response of the LTI system to the input signal
t, y, _ = signal.lsim(sys, u, t) #

# Plot the input and output signals
plt.plot(t, u, label='Input')
plt.plot(t, y, label='Output')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Signal')
plt.show()

import numpy as np

def check_lti(h, t):
    """
    Check if a system is LTI by comparing its impulse response at different times.
    h: the impulse response of the system
    t: the time vector for the impulse response
    Returns True if the system is LTI, False otherwise.
    """
    # Compute the convolution of the impulse response with itself at different times
    for i in range(len(t)):
        for j in range(len(t)):
            if i != j:
                t1, t2 = t[i], t[j]
                h1, h2 = h[i], h[j]
                h1h2 = np.convolve(h1, h2)
                h2h1 = np.convolve(h2, h1)
                if not np.array_equal(h1h2, h2h1):
                    # If the convolution results are not equal, the system is not LTI
                    return False
    return True

print(check_lti(y,t))