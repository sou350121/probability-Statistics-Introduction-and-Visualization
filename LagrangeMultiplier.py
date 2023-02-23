# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:59:23 2023

@author: ken3

Introduction:
    Lagrange multiplier
    L(x,y,λ) = f(x,y) + λg(x,y)
    The variable λ representing the cost of satisfying the constraint. 
    We then take the partial derivatives of the Lagrangian with respect 
    to x, y, and λ, and set them equal to zero.
    
"""

import numpy as np
from scipy.optimize import minimize

def main():
    # Define the objective function and constraints
    def f(x):
        return x[0]**2 + x[1]**2  # Objective function

    def g(x):
        return np.array([x[0] + x[1] - 1, x[0] - x[1]])  # Constraints

    # Use the minimize function from the SciPy library to minimize the Lagrangian
    # The minimize function takes an initial guess for the variables (x0), 
    # the Lagrange multipliers (args), the method for optimization (method), 
    # the constraints (constraints), and some options for the optimization algorithm (options).
    res = minimize(lambda x, l: f(x) + np.dot(l, g(x)), x0=[1, 1], args=(np.zeros(2),),
                   method='SLSQP', constraints={'type': 'eq', 'fun': lambda x: g(x)},
                   options={'ftol': 1e-9, 'disp': False})

    # Print the results
    print(f"Minimum value: {res.fun}")
    print(f"X values: {res.x}")
    print(f"Lagrange multipliers: {res.x}")

if __name__ == "__main__":
    main()