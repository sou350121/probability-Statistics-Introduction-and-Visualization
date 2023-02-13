# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:49:32 2023

@author: ken3

Introduction 
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# Probability distribution function
# Define the mean and standard deviation of the distribution
mean = 0
std = 1

# Generate random values from the normal distribution
x = np.random.normal(mean, std, 1000)

# Calculate the PDF using the scipy library
pdf = stats.norm.pdf(x, mean, std)

# Plot the PDF
plt.hist(x, bins=30, density=True)
plt.plot(x, pdf)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('PDF of a Normal Distribution')
plt.show()

# Probability density function
'''
A function that represents a continuous probability distribution is called a probability density function.
'''
class ProbabilityDensityFunction:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std
    
    def calculate_pdf(self, x):
        return (1 / (self.std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - self.mean) / self.std)**2)
    
    def plot_pdf(self, x):
        y = self.calculate_pdf(x)
        plt.plot(x, y)
        plt.show()
        
pdf = ProbabilityDensityFunction(0, 1)
x = np.linspace(-5, 5, 100)
pdf.plot_pdf(x)