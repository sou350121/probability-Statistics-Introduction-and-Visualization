# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:27:18 2023

@author: ken3

Introduction:
    Moing average
"""

import numpy as np
from scipy.signal import convolve

def moving_average(x, n):
    weights = np.repeat(1.0, n)/n
    return np.convolve(x, weights, mode='valid')

def main():
    # Generate random time series data
    np.random.seed(123)
    data = np.random.randint(0, 300, 50)

    # Compute moving average with order 5
    ma = moving_average(data, 5)

    # Plot original time series data and moving average
    import matplotlib.pyplot as plt
    plt.plot(data, label='Original Data')
    plt.plot(ma, label='Moving Average (Order 5)')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()