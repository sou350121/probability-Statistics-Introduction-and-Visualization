# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:21:01 2023

@author: ken3

Introduction:
    Entropy is a measure of the uncertainty or randomness of an information source.
    H(X) = - Σ p(x) log2 p(x)
    
    Joint entropy is a measure of the amount of information shared by 
    two or more information sources.
    H(X,Y) = - Σ Σ p(x,y) log2 p(x,y)
    
    Conditional entropy is a measure of the amount of uncertainty in 
    one information source given knowledge of another information source.
    H(X|Y) = - Σ Σ p(x,y) log2 p(x|y)
    
    Mutual information is a measure of the amount of information shared by 
    two information sources. It is defined as the reduction in uncertainty of 
    one source given knowledge of the other source.
    I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)
"""

import numpy as np

def entropy(p):
    """Calculates the entropy of an information source."""
    return -np.sum(p * np.log2(p))

def joint_entropy(p):
    """Calculates the joint entropy of two information sources."""
    return -np.sum(p * np.log2(p))

def conditional_entropy(p, q):
    """Calculates the conditional entropy of an information source given another."""
    return joint_entropy(np.concatenate([p, q]).reshape((2, -1)).T) - entropy(q)

def mutual_information(p, q):
    """Calculates the mutual information between two information sources."""
    return entropy(p) - conditional_entropy(p, q)

# Example usage
p = np.array([0.2, 0.3, 0.1, 0.4])
q = np.array([0.5, 0.5])

H_X = entropy(p)
H_Y = entropy(q)
H_XY = joint_entropy(np.outer(p, q).flatten())
H_X_given_Y = conditional_entropy(np.outer(p, q).flatten(), q)
I_XY = mutual_information(np.outer(p, q).flatten(), q)

print(f" The entropy of an information source X: {H_X}")
print(f" The joint entropy of two information sources: {H_XY}")
print(f" The conditional entropy of an information source given: {H_X_given_Y}")
print(f" tThe mutual information between two information sources: {I_XY}")
