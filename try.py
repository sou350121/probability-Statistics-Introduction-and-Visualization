# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:29:41 2023

@author: Administrator
"""

import sympy as sp

t = sp.symbols('t', real=True)
L, R = sp.symbols('L R', positive=True)
tau = sp.symbols('tau')

# Define signals
e = sp.Heaviside(t) - sp.Heaviside(t-1)
h = (1/L)*sp.exp(-R/L*t)*sp.Heaviside(t)

# Compute convolution
i = sp.integrate(e.subs(tau=t-sp.Symbol('t'))*h.subs({t: tau}), (tau, -sp.oo, t))

# Simplify and display result
i = sp.simplify(i)
sp.pprint(i)