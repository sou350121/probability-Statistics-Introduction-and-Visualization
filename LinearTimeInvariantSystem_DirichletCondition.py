# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:10:41 2023

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the Dirichlet boundary function
def dirichlet_boundary(x):
    return np.sin(x)

# Solve the PDE using the Dirichlet condition
def solve_pde_dirichlet():
    # Define the domain and discretization
    x = np.linspace(0, 2*np.pi, 100)
    dx = x[1] - x[0]
    
    # Set the initial condition
    f = np.zeros_like(x)
    f[0] = dirichlet_boundary(x[0])
    
    # Solve the PDE using finite differences
    for i in range(1, len(x)):
        f[i] = f[i-1] + dx*(1-np.cos(f[i-1]))
    
    # Apply the Dirichlet condition at the boundary
    f[0] = dirichlet_boundary(x[0])
    f[-1] = dirichlet_boundary(x[-1])
    
    # Plot the solution
    plt.plot(x, f)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Solution to PDE with Dirichlet condition')
    plt.show()

# Call the solve_pde_dirichlet function to solve and plot the solution
solve_pde_dirichlet()