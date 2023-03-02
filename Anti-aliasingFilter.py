# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:08:13 2023

@author: ken3

Introduction:
    Anti-aliasing filter is a type of signal processing filter that is used to 
    prevent aliasing when a signal is digitized. 
    H(f) ={
        1, |f| < f_c
        0, |f| > f_c
        }
    where H(f) is the frequency response of the filter, f is the frequency, 
    and f_c is the cutoff frequency. 
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Generate a test signal
t = np.linspace(0, 1, 1000, endpoint=False)
x = np.sin(2 * np.pi * 3 * t) + np.sin(2 * np.pi * 15 * t)+ np.sin(2 * np.pi * 20 * t)

# Define the filter parameters
fc = 10  # Cutoff frequency
fs = 30  # Sampling frequency
nyquist = fs / 2  # Nyquist frequency
order = 5  # Filter order

# Design the filter
b, a = signal.butter(order, fc / nyquist, 'lowpass')

# Apply the filter to the signal
y = signal.filtfilt(b, a, x)

# Plot the original and filtered signals
plt.plot(t, x, 'b-', label='Original signal')
plt.plot(t, y, 'r-', label='Filtered signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()