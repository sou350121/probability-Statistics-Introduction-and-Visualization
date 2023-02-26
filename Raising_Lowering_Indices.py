# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 17:41:01 2023

@author: ken3

Introduction:
    Raising and lowering indices is a mathematical technique used in physics to 
    manipulate tensors. Tensors are mathematical objects that generalize 
    vectors and matrices to higher dimensions. They are used to 
    describe physical quantities such as forces, velocities, and electromagnetic fields.
"""
import numpy as np
from sympy import symbols, diag, Matrix

# Define the metric tensor
g = diag(1, -1, -1, -1)

# Define a contravariant vector
A = np.array([1, 2, 3, 4])

# Raise the index of A
g_inv = Matrix(g).inv()
A_up = np.dot(g_inv, A)

# Lower the index of A
A_down = np.dot(g, A_up)

print("Original vector A:", A)
print("Raised index vector A^j:", A_up)
print("Lowered index vector A_j:", A_down)