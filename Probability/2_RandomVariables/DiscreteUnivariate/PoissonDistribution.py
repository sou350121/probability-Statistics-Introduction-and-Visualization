# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:52:07 2023

@author: ken3

Introduction:
    Poisson distribution is a probability distribution that describes 
    the probability of a certain number of events occurring in 
    a fixed interval of time or space, given the average rate of occurrence.
    
    Poisson random variable is a discrete random variable
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def poisson_pmf(k, lambda_):
    return math.exp(-lambda_) * lambda_**k / math.factorial(k)

def poisson_cdf(k, lambda_):
    cdf = 0
    for i in range(k+1):
        cdf += poisson_pmf(i, lambda_)
    return cdf

# Example usage
lambda_ = 5
k_values = np.arange(0, 20)
pmf_values = [poisson_pmf(k, lambda_) for k in k_values]
cdf_values = [poisson_cdf(k, lambda_) for k in k_values]

# Plot PMF and CDF
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(k_values, pmf_values, 'bo', ms=8)
ax1.vlines(k_values, 0, pmf_values, colors='b', lw=5, alpha=0.5)
ax1.set_title('Poisson PMF')
ax1.set_xlabel('k')
ax1.set_ylabel('P(X=k)')

ax2.plot(k_values, cdf_values, 'ro', ms=8)
ax2.vlines(k_values,cdf_values)