# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:53:01 2023

@author: ken3

Introduction:
    Scalar-valued functions are used to describe physical quantities that have 
    a magnitude, but no direction. Examples of scalar-valued functions include 
    temperature, pressure, and energy.

    a vector-valued function is a function that takes input in some 
    vector space and returns a vector as output. The output vector can be 
    in the same vector space as the input or in a different one. 
    Vector-valued functions are used to describe physical quantities that 
    have both magnitude and direction, such as velocity, force, and acceleration. 
    Examples of vector-valued functions include position, velocity, and acceleration.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define a scalar-valued function
def f(x):
    return np.sin(x)

# Define a vector-valued function
def r(t):
    x = np.cos(t)
    y = np.sin(t)
    z = t
    return np.array([x, y, z])

# Visualize the functions
x_vals = np.linspace(-5, 5, 100)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals)
plt.title('Scalar-valued function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

t_vals = np.linspace(0, 10*np.pi, 100)
r_vals = r(t_vals)
plt.plot(r_vals[0], r_vals[1])
plt.title('Vector-valued function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.show()