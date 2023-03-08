# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:20:00 2023

@author: ken3

Introduction
    states that the total variation distance between two probability distributions 
    is bounded below by a function of their Kullback-Leibler divergence.
    The total variation distance between two probability distributions measures 
    the largest possible difference between the probabilities assigned to 
    the same event by the two distributions. 
    
"""

import numpy as np
from scipy.stats import entropy


import matplotlib.pyplot as plt

def plot_pinsker_inequality(p, q):
    alphas = np.linspace(0, 1, 100)
    tv_distances = [total_variation_distance((1 - alpha) * p + alpha * q, p) for alpha in alphas]
    kl_divergences = [entropy((1 - alpha) * p + alpha * q, q) for alpha in alphas]

    fig, ax = plt.subplots()
    ax.plot(alphas, tv_distances, label="Total variation distance")
    ax.plot(alphas, kl_divergences, label="Kullback-Leibler divergence")
    ax.set_xlabel("Interpolation parameter alpha")
    ax.legend()
    plt.show()

p = np.array([0.3, 0.5, 0.2])
q = np.array([0.2, 0.6, 0.2])

plot_pinsker_inequality(p, q)