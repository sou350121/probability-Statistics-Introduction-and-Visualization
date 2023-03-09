# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 09:31:55 2023

@author: ken3

Introduction:
    Rotation matrix is a linear transformation in which an object is rotated about a certain point or axis. 
    R_x = | 1       0              0         |
      | 0  cos(theta_x) -sin(theta_x) |
      | 0  sin(theta_x)  cos(theta_x) |

    R_y = | cos(theta_y)  0  sin(theta_y) |
      |      0        1      0       |
      |-sin(theta_y)  0  cos(theta_y) |

    R_z = | cos(theta_z) -sin(theta_z) 0 |
      | sin(theta_z)  cos(theta_z) 0 |
      |     0              0        1 |

    R = R_z * R_y * R_x
"""

import numpy as np

def rotation_matrix(theta_x, theta_y, theta_z):
    # Conversion of angles to radians
    rad_x = theta_x * np.pi / 180
    rad_y = theta_y * np.pi / 180
    rad_z = theta_z * np.pi / 180

    # Calculation of rotation matrices along x, y, and z axes
    R_x = np.array([[1, 0, 0],
                    [0, np.cos(rad_x), -np.sin(rad_x)],
                    [0, np.sin(rad_x), np.cos(rad_x)]])

    R_y = np.array([[np.cos(rad_y), 0, np.sin(rad_y)],
                    [0, 1, 0],
                    [-np.sin(rad_y), 0, np.cos(rad_y)]])

    R_z = np.array([[np.cos(rad_z), -np.sin(rad_z), 0],
                    [np.sin(rad_z), np.cos(rad_z), 0],
                    [0, 0, 1]])

    # Final rotation matrix as a product of rotation matrices along x, y, and z axes
    R = np.dot(R_z, np.dot(R_y, R_x))
    return R

def main():
    # Example usage
    theta_x = 30    # degrees
    theta_y = 45    # degrees
    theta_z = 60    # degrees
    R = rotation_matrix(theta_x, theta_y, theta_z)
    print(R)
    # Note that in the above code, we have used the dot function of NumPy to 
    # calculate the product of rotation matrices.

if __name__ == "__main__":
    main()