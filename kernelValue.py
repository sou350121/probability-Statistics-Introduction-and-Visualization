# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:47:03 2023

@author: ken3

Introduction 
    kernel values
"""

import numpy as np
import matplotlib.pyplot as plt

# Define a Gaussian kernel function
def gaussian_kernel(x, y, sigma=1.0):
    return np.exp(-np.linalg.norm(x - y)**2 / (2 * sigma**2))

# Create a 1D grid of points
x_grid = np.linspace(-5, 5, 100)

# Compute the kernel values for a pair of points
x1 = -2
x2 = 3
kernel_values = [gaussian_kernel(x1, x, sigma=1.0) * gaussian_kernel(x2, x, sigma=1.0) for x in x_grid]

# Visualize the kernel values
plt.plot(x_grid, kernel_values)
plt.xlabel("x")
plt.ylabel("Kernel values")
plt.title("Gaussian Kernel Visualization")
plt.show()