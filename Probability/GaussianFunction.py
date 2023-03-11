# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:40:03 2023

@author: ken3
    
Introduction
    f(x) = (1/σ√2π) * e^-(x-μ)^2/2σ^2

    where:
    
    x is the random variable
    μ is the mean of the distribution
    σ is the standard deviation of the distribution
    e is Euler's number, approximately equal to 2.71828
"""

import numpy as np

def gaussian(x, mu, sigma):
    return 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2*sigma**2))


import matplotlib.pyplot as plt

# Generate a range of input values
x = np.linspace(-5, 5, 100)

# Calculate the Gaussian function for the input values with mean=0 and sigma=1
y = gaussian(x, 0, 1)

# Plot the Gaussian curve
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gaussian function')
plt.show()