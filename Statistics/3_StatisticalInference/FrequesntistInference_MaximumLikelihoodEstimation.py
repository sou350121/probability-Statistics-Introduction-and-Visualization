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
    
    Likelihood L(theta|x) = f(x|theta)
    where f(x|theta) is the probability density function of the observed data x given the model parameters theta.
    
Ref:
    https://analyticsindiamag.com/maximum-likelihood-estimation-python-guide/
"""

import numpy as np
from scipy.stats import norm

# Generate some normally distributed data
np.random.seed(1)
data = np.random.normal(loc=5, scale=2, size=300)

# Define the likelihood function for a normal distribution
def likelihood_function(params):
    mu, sigma = params
    # use the logpdf method to compute the log-likelihood and sum the values
    return np.sum(norm.logpdf(data, loc=mu, scale=sigma))

# Find the maximum likelihood estimates using the minimize function
from scipy.optimize import minimize

result = minimize(lambda params: -likelihood_function(params), x0=[0, 1],method='L-BFGS-B')
mu_mle, sigma_mle = result.x

print(f"mu_mle = {mu_mle:.2f}, sigma_mle = {sigma_mle:.2f}")

import matplotlib.pyplot as plt

# Plot the data
plt.hist(data, bins=20, density=True)

# Generate x values for the PDF plot
x = np.linspace(-5, 15, 1000)

# Plot the PDF with the estimated parameters
pdf = norm.pdf(x, loc=mu_mle, scale=sigma_mle)
plt.plot(x, pdf, 'r-', label='PDF (MLE)')

plt.legend()
plt.show()