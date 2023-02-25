# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 15:08:02 2023

@author: ken3

Introduction:
    A Venn diagram is a visual representation of the relationships between sets.
    
    install matplotlib_venn for visualization. 
    "pip install matplotlib_venn"
"""

from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt

# Define the sets
A = set([1, 2, 3, 4, 5])
B = set([3, 4, 5, 6, 7])

# Create the Venn diagram
venn2([A, B], set_colors=('blue', 'green'), set_labels=('Set A', 'Set B'))

# Show the plot
plt.show()

## Venn3 for 3 sets

C = set([1, 2, 3, 6, 7])

venn3([A, B, C], set_colors=('blue', 'green','red'), set_labels=('Set A', 'Set B','Set C'))
# Show the plot
plt.show()