# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:29:41 2023

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

def anti_aliasing_filter(signal, cutoff_frequency, sampling_frequency):
    nyquist_frequency = sampling_frequency / 2
    normalized_cutoff_frequency = cutoff_frequency / nyquist_frequency
    num_samples = len(signal)
    signal_fft = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(num_samples, d=1/sampling_frequency)
    mask = np.abs(frequencies) < normalized_cutoff_frequency
    signal_fft[~mask] = 0
    filtered_signal = np.fft.ifft(signal_fft)
    return filtered_signal.real

# Generate a random sine wave signal
sampling_frequency = 1000
t = np.linspace(0, 1, sampling_frequency)
signal = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 20 * t) + np.sin(2 * np.pi * 30 * t)

# Apply the anti-aliasing filter
cutoff_frequency = 15
filtered_signal = anti_aliasing_filter(signal, cutoff_frequency, sampling_frequency)

# Plot the original and filtered signals
plt.subplot(211)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(212)
plt.plot(t, filtered_signal)
plt.title('Filtered Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()