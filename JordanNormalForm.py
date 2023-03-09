# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:53:56 2023

@author: ken3

Introduction:
    Jordan normal form is a way to represent a square matrix as a sum of diagonal matrices and 
    matrices composed of ones and zeros.
    
    M = P * J * P^-1
    where M is the square matrix to be transformed, 
    P is the matrix consisting of the eigenvectors of M, J is 
    the Jordan normal form of M, and P^-1 is the inverse of P.
"""

import numpy as np

def jordan_normal_form(m):
    # Eigendecomposition of the input matrix
    eigenvalues, eigenvectors = np.linalg.eig(m)

    # Sorting the eigenvalues and corresponding eigenvectors
    indices = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[indices]
    eigenvectors = eigenvectors[:, indices]

    # Initialization of Jordan normal form and computation of the diagonal blocks
    jordan = np.zeros_like(m)
    i = 0
    while i < m.shape[0]:
        if i+1 < m.shape[0] and abs(m[i+1][i]) > 0.00001:
            jordan[i][i] = eigenvalues[i]
            jordan[i+1][i+1] = eigenvalues[i]
            jordan[i+1][i] = 1
            jordan[i][i+1] = 0
            i += 2
        else:
            jordan[i][i] = eigenvalues[i]
            i += 1

    # Matrix of eigenvectors
    P = eigenvectors

    # Inverse of P
    P_inv = np.linalg.inv(P)

    # Transforming the input matrix to its Jordan normal form
    jordan_normal_form = np.dot(np.dot(P, jordan), P_inv)

    return jordan_normal_form

def main():
    # Example usage
    m = np.array([[3, -1, 0], [1, 2, 1], [-1, -1, 2]])
    jordan = jordan_normal_form(m)
    print(jordan)

if __name__ == "__main__":
    main()