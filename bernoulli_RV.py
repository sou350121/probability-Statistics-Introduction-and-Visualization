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
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import bernoulli

# Generate a Bernoulli random variable with probability of success p = 0.7
rv = bernoulli(0.7)

# Generate 1000 samples from the Bernoulli distribution
data = rv.rvs(1000)

# Plot the data using a histogram
sns.histplot(data, kde=True)
plt.savefig('bernoulli_histogram.png')

# Show the plot
plt.show()