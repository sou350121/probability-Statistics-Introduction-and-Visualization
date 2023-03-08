# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:55:19 2023

@author: ken3

Introduction:
     also known as maximum a posteriori (MAP) estimator, is a method used to 
     estimate the parameters of a statistical model based on a Bayesian approach. 
     In this method, we incorporate prior knowledge or belief about 
     the parameter values into the estimation process.
     
     θ_MAP = argmax p(θ|X) = argmax p(X|θ)p(θ)
     where θ is the parameter of interest, X is the observed data, p(X|θ) is 
     the likelihood function, and p(θ) is the prior distribution over θ.
"""

import numpy as np
from scipy.stats import norm

# Generate some normally distributed data
data = np.random.normal(loc=5, scale=2, size=100)

# Define the likelihood function for a normal distribution
def likelihood_function(params):
    mu, sigma = params
    return np.sum(norm.logpdf(data, loc=mu, scale=sigma))

# Define the prior distribution for the mean
def prior_function(mu):
    return norm.logpdf(mu, loc=0, scale=1)

# Define the posterior function
def posterior_function(params):
    mu, sigma = params
    return likelihood_function(params) + prior_function(mu)

# Find the maximum posterior estimates using the minimize function
from scipy.optimize import minimize

result = minimize(lambda params: -posterior_function(params), x0=[1, 1],method='L-BFGS-B')
mu_map, sigma_map = result.x

print(f"mu_map = {mu_map:.2f}, sigma_map = {sigma_map:.2f}")

import matplotlib.pyplot as plt

# Plot the data
plt.hist(data, bins=20, density=True)

# Generate x values for the PDF plot
x = np.linspace(-5, 15, 1000)

# Plot the PDF with the estimated parameters
pdf = norm.pdf(x, loc=mu_map, scale=sigma_map)
plt.plot(x, pdf, 'r-', label='PDF (MAP)')

plt.legend()
plt.show()