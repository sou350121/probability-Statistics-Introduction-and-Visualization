# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:16:49 2023

@author: ken3

Introduction
"""
import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, x0, y0, h, n):
    """
    Euler method for approximating the solution to a first-order differential equation
    
    Parameters:
    f: function - the derivative of y with respect to x
    x0: float - the initial value of x
    y0: float - the initial value of y
    h: float - the step size
    n: int - the number of subintervals to calculate
    
    Returns:
    x: array - the x-values of the approximation
    y: array - the y-values of the approximation
    """
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = x0
    y[0] = y0
    
    for i in range(1, n+1):
        x[i] = x[i-1] + h
        y[i] = y[i-1] + h*f(x[i-1], y[i-1])
        
    return x, y


def f(x, y):
    return -2*x*y

x, y = euler_method(f, -1, 1, 0.1, 20)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler Method Approximation')
plt.show()
