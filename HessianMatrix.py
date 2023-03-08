# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:33:24 2023

@author: ken3

Introduction:
    The Hessian matrix is a square matrix of second-order partial derivatives of
    a multivariable function. 
    In other words, the Hessian matrix tells us how a function is changing 
    in all directions around a given point, and whether the function is 
    convex, concave, or neither at that point.
    
    The Hessian matrix H of a function f(x1, x2, ..., xn) is an n×n matrix, 
    where H_ij = ∂²f/∂xi∂xj.
"""

import sympy

# Define a multivariable function
x, y = sympy.symbols('x y')
f = x**3 + y**2 - x*y

# Compute the Hessian matrix of the function
hessian = sympy.Matrix([[sympy.diff(f, x, x), sympy.diff(f, x, y)],
                        [sympy.diff(f, y, x), sympy.diff(f, y, y)]])
print("Hessian matrix:\n", hessian)

# Evaluate the Hessian matrix at a particular point
point = {x: 1, y: 2}
hessian_at_point = hessian.subs(point)
print("Hessian matrix at point", point, ":\n", hessian_at_point)


# numpy example
import numpy as np

def hessian(x):
    """
    Calculate the hessian matrix with finite differences
    Parameters:
       - x : ndarray
    Returns:
       an array of shape (x.dim, x.ndim) + x.shape
       where the array[i, j, ...] corresponds to the second derivative x_ij
    """
    x_grad = np.gradient(x) 
    hessian = np.empty((x.ndim, x.ndim) + x.shape, dtype=x.dtype) 
    for k, grad_k in enumerate(x_grad):
        # iterate over dimensions
        # apply gradient again to every component of the first derivative.
        tmp_grad = np.gradient(grad_k) 
        for l, grad_kl in enumerate(tmp_grad):
            hessian[k, l, :, :] = grad_kl
    return hessian

x = np.random.randn(100, 100, 100)
print("Hessian matrix for 3D normal distribution:", hessian(x))