# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 10:38:10 2023

@author: ken3

Introduction:
    also known as the Sampling Theorem or the Whittaker-Shannon interpolation formula, 
    is a fundamental theorem in signal processing that describes 
    the minimum sampling rate required to accurately reconstruct 
    a continuous-time signal from its samples. It states that 
    a continuous-time signal can be reconstructed perfectly from its samples 
    if the sampling rate is at least twice the maximum frequency present in the signal.

    x(t) = ∑n x[n]sinc((t - nT)/T)
    where T = 1/fs is the sampling period, sinc is the sinc function, and x[n] 
    are the samples of the continuous-time signal x(t) taken at the times nT.
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