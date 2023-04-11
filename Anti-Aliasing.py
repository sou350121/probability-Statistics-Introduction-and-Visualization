# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:45:04 2023

@author: ken3

Introduction
"""

from sympy import *
init_printing()

# Define symbols
t, w = symbols('t omega', real=True)
T = Rational(1, 4)
w0 = 2 * pi / T
n = symbols('n', integer=True)

# Define signal xc(t)
xc = Piecewise((1, Abs(w) <= w0), (0, True))

# Define Ha(jw)
Ha = Piecewise((1, Abs(w) <= 4 * pi), (0, True))

# Define x1(t)
x1 = 4 * pi * Sum(xc.subs(w, n * w0) * sinc((w - n * w0) * T), (n, -oo, oo))

# Define x2(t)
x2 = 4 * pi * Sum(xc.subs(w, n * w0) * Ha.subs(w, w - n * w0) * sinc((w - n * w0) * T), (n, -oo, oo))

# Define energy of xc(t)
E_xc = integrate(xc ** 2, (w, -oo, oo))

# Define energy of reconstruction errors
E1 = integrate((xc - x1) ** 2, (t, -oo, oo))
E2 = integrate((xc - x2) ** 2, (t, -oo, oo))

# Display results
display(E_xc)
display(E1)
display(E2)

# Prove that there is no other signal that could come out of the D->C converter that is closer to xc(t) than x2(t)
# Here closer means that the energy in the error is smaller.
# Assume that there exists another signal y(t) that is closer to xc(t) than x2(t)
# Then, we have E_xc - E2 < E_xc - E_y
# Therefore, E_y < E2
# But, we know that x2(t) is the best approximation of xc(t) that can be obtained using the D->C converter and Ha(jw)
# Therefore, there cannot exist another signal y(t) that is closer to xc(t) than x2(t)
