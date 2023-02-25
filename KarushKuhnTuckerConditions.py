# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:25:17 2023

@author: ken3

Introduction:
    KKT conditions is a set of necessary conditions for optimization problems that include constraints. 
    it states that the optimal solution to an optimization problem with 
    constraints must satisfy three conditions:
        
    Stationarity: The gradient of the objective function must be equal to 
    a linear combination of the gradients of the constraint functions, 
    weighted by Lagrange multipliers.
    `∇f(x) = ∑ λi ∇gi(x)   for i=1,2,...,m`

    Primal feasibility: The constraint functions must be satisfied.
    `gi(x) ≤ 0   for i=1,2,...,m`

    Dual feasibility: The Lagrange multipliers must be non-negative.
    `λi ≥ 0   for i=1,2,...,m  λi * gi(x) = 0   for i=1,2,...,m`
"""

import numpy as np
from scipy.optimize import minimize

# Define the objective function to be optimized
def objective(x):
    return x[0]**2 + x[1]**2

# Define the constraint functions
def constraint1(x):
    return x[0] + x[1] - 1

def constraint2(x):
    return x[0] - x[1] - 2

# Define the constraints using dictionaries
eq_cons = {'type': 'eq', 'fun': constraint1}
ineq_cons = {'type': 'ineq', 'fun': constraint2}

# Combine the constraints into a list
constraints = [eq_cons, ineq_cons]

# Find the minimum of the objective function subject to the constraints
result = minimize(objective, [0, 0], constraints=constraints)

print("Optimal solution:", result.x)
print("Optimal value:", result.fun)