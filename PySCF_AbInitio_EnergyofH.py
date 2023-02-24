# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:40:27 2023

@author: ken3
"""

import pyscf

mol = pyscf.gto.M(atom='H 0 0 0; H 0 0 0.74', basis='sto-3g')
mf = pyscf.scf.RHF(mol)
energy = mf.kernel()
print('Energy:', energy)

import matplotlib.pyplot as plt
import numpy as np

grid = pyscf.dft.gen_grid.Grids(mol)
grid.atom_grid = (99, 590)
grid.becke_scheme = pyscf.dft.gen_grid.stratmann
grid.prune = None
grid.build()

ao = pyscf.dft.numint.eval_ao(mol, grid.coords)
rho = pyscf.dft.numint.eval_rho(mol, ao, mf.make_rdm1())
rho.shape = grid.weights.shape

fig, ax = plt.subplots()
ax.scatter(grid.coords[:, 0], grid.coords[:, 1], c=rho, s=1)
plt.show()