# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 00:15:32 2023

@author: ken3

Introdution
    
"""

import numpy as np

def convolve(x, h):
    """
    Computes the convolution of two sequences x and h.
    """
    N = len(x)
    M = len(h)
    y = np.zeros(N+M-1)
    for n in range(N+M-1):
        for k in range(max(0, n-M+1), min(N, n+1)):
            y[n] += x[k] * h[n-k]
    return y

x = np.array([1, 2, 3])
h = np.array([1, 1, 1])
y = convolve(x, h)
print(y)