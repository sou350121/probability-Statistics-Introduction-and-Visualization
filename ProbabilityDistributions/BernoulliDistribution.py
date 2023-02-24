# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 08:58:06 2023

@author: ken3
"""

'''
use the scipy.stats module to generate a Bernoulli random variable and 
the seaborn library to visualize it. 

A Bernoulli random variable is a discrete probability distribution that takes 
on one of two values, typically represented as 0 or 1, with a probability of 
success, denoted by p, and a probability of failure, denoted by 1-p. 
The probability mass function (PMF) of a Bernoulli random variable is given by:

P(X = x) = p^x * (1-p)^(1-x)

where x = 0 or 1.

'''
import scipy.stats as stats

p = 0.6  # probability of success

# pmf
def bernoulli_pmf(x):
    return stats.bernoulli.pmf(x, p)

# cdf
def bernoulli_cdf(x):
    return stats.bernoulli.cdf(x, p)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(2)  # possible values of X

# plot pmf
plt.stem(x, bernoulli_pmf(x))
plt.xlabel('x')
plt.ylabel('P(X = x)')
plt.title('Bernoulli PMF (p = 0.7)')

# plot cdf
plt.figure()
plt.step(x, bernoulli_cdf(x))
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Bernoulli CDF (p = 0.7)')

plt.show()