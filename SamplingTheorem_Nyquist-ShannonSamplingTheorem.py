# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:38:10 2023

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

# Define a continuous-time signal
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t)

# Plot the continuous-time signal
plt.figure()
plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Continuous-Time Signal')

# Define the sampling frequency
fs = 30

# Sample the continuous-time signal at the given sampling frequency
n = np.arange(0, len(t), int(fs/5))
x_sampled = x[n]

# Plot the sampled signal
plt.figure()
plt.stem(n/fs, x_sampled)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sampled Signal')

# Reconstruct the signal using zero-order hold interpolation
t_recon = np.linspace(0, 1, int(fs))
x_recon = np.zeros(len(t_recon))
for i in range(len(n)):
    x_recon[i*int(fs/5):(i+1)*int(fs/5)] = x_sampled[i]

# Plot the reconstructed signal
plt.figure()
plt.plot(t_recon, x_recon)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Reconstructed Signal')

plt.show()