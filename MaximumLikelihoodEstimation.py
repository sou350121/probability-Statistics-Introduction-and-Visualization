# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 22:41:03 2023

@author: ken3

Introduction:
    The basic idea behind MLE is to find the parameter values that make the observed data most likely. 
    This is done by calculating the likelihood function, which is 
    a function that describes the probability of observing 
    the data given the parameter values. The likelihood function is then 
    maximized with respect to the parameters to find the parameter values 
    that make the data most likely.
"""

import numpy as np
from scipy.stats import norm
from scipy.optimize import minimize

# Generate some data from a normal distribution
np.random.seed(0)
data = np.random.normal(3, 2, size=100)

# Define the likelihood function for a normal distribution
def likelihood(params):
    mu, sigma = params
    return -np.sum(norm.logpdf(data, loc=mu, scale=sigma))

# Find the maximum likelihood estimates for the normal distribution
initial_guess = [0, 1] # starting values for the parameters
result = minimize(likelihood, initial_guess)
mu_mle, sigma_mle = result.x

print("Maximum likelihood estimates:")
print("mu =", mu_mle)
print("sigma =", sigma_mle)