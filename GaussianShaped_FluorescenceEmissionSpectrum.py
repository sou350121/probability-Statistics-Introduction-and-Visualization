# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 13:04:17 2023

@author: ken3

Introduction:
    
    This code generates a plot of a Gaussian-shaped fluorescence spectrum centered 
    at 525 nm with a width of 25 nm. The intensity of the spectrum is set to 1.0. 
    The resulting plot shows the fluorescence intensity as a function of wavelength in nanometers.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
wavelengths = np.arange(400, 700, 1)
center = 525  # center wavelength
width = 25    # spectral width
intensity = 1.0   # peak intensity

# Generate Gaussian-shaped spectrum
spectrum = intensity * np.exp(-(wavelengths - center)**2 / (2 * width**2))

# Plot spectrum
plt.plot(wavelengths, spectrum)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Fluorescence intensity')
plt.show()