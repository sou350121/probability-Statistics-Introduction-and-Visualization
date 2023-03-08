# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:39:01 2023

@author: ken3

Introduction:
    Two measure of how different two probability distributions are from each other. 
    
    KL-divergence measures the amount of information lost when using 
    one probability distribution to approximate another.
    
    Wasserstein distance measures the minimum amount of "work" required to 
    transform one probability distribution into another. In this context, "work"
    refers to the amount of mass that needs to be moved from one point in 
    the distribution to another in order to transform it into the other distribution.
"""

import numpy as np
from scipy.stats import wasserstein_distance


def kl_divergence(p, q):
    return np.sum(p * np.log(p / q))

p = np.array([0.2, 0.3, 0.5])
q = np.array([0.4, 0.4, 0.2])

kl = kl_divergence(p, q)
wd = wasserstein_distance(p, q)

print("KL distance between P and Q:", kl)
print("Wasserstein distance between P and Q:", wd)