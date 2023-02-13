# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:35:09 2023

@author: Administrator
"""

import numpy as np

class PauliExclusionPrinciple:
    def __init__(self, num_electrons):
        self.num_electrons = num_electrons
        self.energies = np.zeros(num_electrons)
        self.angular_momenta = np.zeros(num_electrons)
        self.magnetic_quantum_numbers = np.zeros(num_electrons)
        self.spin_quantum_numbers = np.zeros(num_electrons)
    
    def calculate_quantum_numbers(self):
        for i in range(self.num_electrons):
            self.energies[i] = np.random.randint(0, 10)
            self.angular_momenta[i] = np.random.randint(0, 10)
            self.magnetic_quantum_numbers[i] = np.random.randint(0, 10)
            self.spin_quantum_numbers[i] = np.random.randint(0, 2)
    
    def check_exclusion_principle(self):
        for i in range(self.num_electrons):
            for j in range(i + 1, self.num_electrons):
                if (self.energies[i] == self.energies[j] and
                    self.angular_momenta[i] == self.angular_momenta[j] and
                    self.magnetic_quantum_numbers[i] == self.magnetic_quantum_numbers[j]):
                    if self.spin_quantum_numbers[i] == self.spin_quantum_numbers[j]:
                        print("Violation of Pauli exclusion principle!")
                        return False
        print("Pauli exclusion principle is satisfied.")
        return True

p = PauliExclusionPrinciple(3)
p.calculate_quantum_numbers()
p.check_exclusion_principle()
print(f'energies: {p.energies}')
print(f'angular_momenta: {p.angular_momenta}')
print(f'magnetic_quantum_numbers: {p.magnetic_quantum_numbers}')
print(f'spin_quantum_numbers: {p.spin_quantum_numbers}')