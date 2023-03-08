# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:00:35 2023

@author: ken3

Introduction:
    a matrix of partial derivatives used in multivariable calculus to 
    transform vectors from one coordinate system to another. 
    J = ∂(f1, f2, ..., fn) / ∂(x1, x2, ..., xn)
    where f1, f2, ..., fn are functions of the variables x1, x2, ..., xn.
    
    The determinant of the Jacobian matrix, denoted by det(J) or |J|, 
    is a scalar value that provides information about the relationship between 
    the original and transformed coordinate systems. 
    |J| = ad - bc
    It is an important quantity in the study of change of variables in multiple integrals.
    if det(J(f)) ≠ 0 at a point x₀, then the function f is invertible near x₀ and 
    the local behavior of f can be characterized by the inverse function theorem. 
    If det(J(f)) = 0 at x₀, then f is not invertible near x₀ and 
    the local behavior of f is more complicated.
"""

import sympy as sp

# Define the variables and functions
x, y = sp.symbols('x y')
f1 = x**2 + y**2
f2 = sp.exp(x*y)

# Define the Jacobian matrix
J = sp.Matrix([f1, f2]).jacobian([x, y])

# Calculate the determinant of the Jacobian matrix
det_J = J.det()

# Print the results
print("Jacobian matrix:")
print(J)
print("Determinant of the Jacobian matrix:")
print(det_J)


