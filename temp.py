# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:16:40 2023

@author: ken3
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 7)
pmf = np.ones(6) / 6

plt.stem(x, pmf)
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title('Probability Mass Function')
plt.show()