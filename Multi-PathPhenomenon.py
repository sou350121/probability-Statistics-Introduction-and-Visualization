# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:31:49 2023

@author: Administrator
"""

from sympy import *
init_printing()

# Define symbols
t, w = symbols('t omega', real=True)
T = Rational(1, 4)

# Define signals
xc = Piecewise((1, Abs(t) < pi), (0, True))
x1 = Sum(xc * sin(pi * (t - k * T)) / (pi * (t - k * T)), (k, -oo, oo))
x2 = x1 * (sin(pi * t / T) / (pi * t / T))

# Define Fourier transforms
XC = fourier_transform(xc, t, w)
X1 = fourier_transform(x1, t, w)
X2 = fourier_transform(x2, t, w)

# Define Ha
Ha = Piecewise((1, Abs(w) < 2 * pi / T), (0, True))

# Define energy of reconstruction error
E1 = integrate(Abs(xc - x1) ** 2, (t, -oo, oo))
E2 = integrate(Abs(xc - x2) ** 2, (t, -oo, oo))

# Apply Parseval's theorem
E1 = E1.subs(Abs(xc - x1) ** 2, Abs(XC - X1) ** 2)
E1 = E1.subs(Abs(XC) ** 2, Abs(XC) ** 2)
E1 = E1.subs(Abs(X1) ** 2, Abs(X1) ** 2)
E1 = E1.subs(X1, XC * Ha)
E1 = E1.subs(Ha, Piecewise((1, Abs(w) < 2 * pi / T), (0, True)))
E1 = E1.subs(XC, Sum(XC * exp(-I * w * k * T), (k, -oo, oo)))
E1 = E1.subs(Abs(XC) ** 2, Sum(Abs(XC) ** 2, (k, -oo, oo)))
E1 = E1.subs(conjugate(XC), Sum(conjugate(XC) * exp(I * w * k * T), (k, -oo, oo)))
E1 = E1.subs(conjugate(XC) * XC, Abs(XC) ** 2)
E2 = E2.subs(Abs(xc - x2) ** 2, Abs(XC - X2) ** 2)
E2 = E2.subs(Abs(XC) ** 2, Abs(XC) ** 2)
E2 = E2.subs(Abs(X2) ** 2, Abs(X2) ** 2)
E2 = E2.subs(X2, XC * Ha)
E2 = E2.subs(Ha, Piecewise((1, Abs(w) < 2 * pi / T), (0, True)))
E2 = E2.subs(XC, Sum(XC * exp(-I * w * k * T), (k, -oo, oo)))
E2 = E2.subs(Abs(XC) ** 2, Sum(Abs(XC) ** 2, (k, -oo, oo)))
E2 = E2.subs(conjugate(XC), Sum(conjugate(XC) * exp(I * w * k * T), (k, -oo, oo)))
E2 = E2.subs(conjugate(XC) * XC, Abs(XC) ** 2)
# Print results
print("Energy of reconstruction error for x1:", simplify(E1))
print("Energy of reconstruction error for x2:", simplify(E2))