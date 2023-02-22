# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 08:07:09 2023

@author: ken3

Introduction
    ∂f(x, v, t) / ∂t + v · ∇ₓf(x, v, t) + (F(x, t) / m) · ∇ᵛf(x, v, t) = C[f(x, v, t)]
    where:
    - ∂f / ∂t is the time derivative of the PDF
    - v · ∇ₓf is the spatial derivative of the PDF in the direction of the velocity
    - (F / m) · ∇ᵛf is the spatial derivative of the PDF in the direction of the force, divided by the mass of the particle
    - C[f] is the collision operator that accounts for collisions between particles and their effect on the PDF
    
    The Boltzmann equation is a partial differential equation that is difficult to 
    solve analytically. In practice, it is often solved numerically 
    using computational methods such as Monte Carlo simulation or 
    molecular dynamics simulation.
    we simulate a gas of particles in a one-dimensional box using 
    a Monte Carlo method. 
"""

import numpy as np

# Define the parameters of the gas
k_B = 1.38e-23  # Boltzmann constant
T = 300         # temperature in Kelvin
m = 1.0         # mass of the particles

# Define the simulation parameters
N = 1000        # number of particles
L = 1.0e-6      # length of the box
dt = 1.0e-9     # time step
t_max = 1.0e-6  # simulation time

# Initialize the positions and velocities of the particles
x = np.linspace(0, L, N)
v = np.random.normal(loc=0.0, scale=np.sqrt(k_B*T/m), size=N)

# Define the force acting on the particles (in this case, no force)
F = np.zeros_like(x)

# Define the collision operator (in this case, a simple relaxation model)
tau = 1.0e-8  # relaxation time
def collision_operator(f):
    f_eq = np.exp(-m*v**2/(2*k_B*T))/(np.sqrt(2*np.pi*m*k_B*T))
    return (f_eq - f)/tau

# Define the time evolution of the distribution function using the Euler method
f = np.exp(-m*v**2/(2*k_B*T))/(np.sqrt(2*np.pi*m*k_B*T))
for t in np.arange(0, t_max, dt):
    f += dt*(-v*np.gradient(f, x) + F*np.gradient(f, v) + collision_operator(f))

# Calculate the density and temperature of the gas
rho = np.sum(f)/L
T_gas = m*np.sum(v**2*f)/(3*N*k_B)

print("Gas density: {:.2e} kg/m^3".format(rho))
print("Gas temperature: {:.2f} K".format(T_gas))