# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:51:48 2023

@author: ken3

Introduction:
    also known as Gauss's theorem, relates a surface integral over 
    a closed surface to a volume integral over the region enclosed by the surface.
    
    the theorem states that the total flux of a vector field through 
    a closed surface is equal to the volume integral of the divergence of 
    the vector field over the region enclosed by the surface.
    
    ∬S F · dS = ∭V ∇ · F dV
    where S is a closed surface that encloses a region V, F is a vector field 
    defined over V, dS is an infinitesimal surface element of S, and dV is 
    an infinitesimal volume element of V.
"""

# Sympy 
# Better don't use numpy and sympy in the same time
from sympy import symbols, diff, sin, cos, integrate, pi

def main():
    # Define the vector field F
    x, y, z = symbols('x y z')
    F = x**3, y**3, z**3
    print("The symbolic of F:", F)
    # Calculate the divergence of F
    div_F = diff(F[0], x) + diff(F[1], y) + diff(F[2], z)
    print("Divergence of F:", div_F)

    # Calculate the triple integral of the divergence of F over the unit sphere
    rho, phi, theta = symbols('rho phi theta')
    div_F_sph = div_F.subs([(x, rho*sin(phi)*cos(theta)), (y, rho*sin(phi)*sin(theta)), (z, rho*cos(phi))])
    print("Divergence of F_sph", div_F_sph)
    integral = integrate(div_F_sph * rho**2 * sin(phi), (rho, 0, 1), (phi, 0, pi), (theta, 0, 2*pi))
    print("Triple integral of div F over the unit sphere:", integral)

    # Calculate the flux of F through the unit sphere using the Divergence Theorem
    flux = integral
    print("Flux of F through the unit sphere:", flux)

if __name__ == '__main__':
    main()