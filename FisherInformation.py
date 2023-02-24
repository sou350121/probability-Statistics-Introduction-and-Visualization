# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:18:33 2023

@author: ken3

Introduction:
    a measure of the amount of information that an observable random variable X
    carries about an unknown parameter θ that describes the distribution of X. 
    It measures how well the parameter can be estimated based on observations of X.
    
    I(θ) = E[(∂/∂θ)log f(X;θ)]²
    where f(X;θ) is the probability density function (PDF) or 
    probability mass function (PMF) of X, and E[·] denotes the expected value.
    
    This will plot the Fisher information as a function of the parameter p. 
    You can see that the Fisher information is highest at p=0.5, 
    which is the true parameter value, and decreases as p moves away from 0.5.
"""

from scipy.stats import bernoulli

# Define a Bernoulli distribution with parameter p
p = 0.5
dist = bernoulli(p)

# Calculate the Fisher information
theta = p  # The parameter we're interested in
n = 1000  # Sample size
x = dist.rvs(n)  # Generate n random samples from the distribution
loglik = sum([bernoulli.logpmf(xi, theta) for xi in x])  # Log-likelihood function
dloglik = sum([bernoulli.pmf(xi, theta) / theta - 
               bernoulli.pmf(xi, theta) / (1 - theta) for xi in x])  # Derivative of the log-likelihood function
I_p05 = (dloglik / n) ** 2 / (-loglik / n)  # Fisher information

import numpy as np
import matplotlib.pyplot as plt

# Calculate the Fisher information for different values of p
ps = np.linspace(0, 1, 100)
I = np.zeros_like(ps)
for i, p in enumerate(ps):
    dist = bernoulli(p)
    loglik = sum([bernoulli.logpmf(xi, p) for xi in x])
    dloglik = sum([bernoulli.pmf(xi, p) / p - bernoulli.pmf(xi, p) / (1 - p) for xi in x])
    I[i] = (dloglik / n) ** 2 / (-loglik / n)

# Plot the Fisher information
plt.plot(ps, I)
plt.xlabel('p')
plt.ylabel('I(p)')
plt.title('Fisher information for a Bernoulli distribution')
plt.show()