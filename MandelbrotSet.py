# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:16:21 2023

@author: ken3

Reference:
    
"""

import taichi as ti
from taichi.math import cmul, dot, log2, vec2, vec3
ti.init(arch=ti.cpu)

width, height = 800, 640
pixels = ti.Vector.field(3, float, shape=(width, height))

@ti.func
def setcolor(z, i):
    v = log2(i + 1 - log2(log2(z.norm()))) / 5
    col = vec3(0)
    if v < 1.0:
        col = vec3(v**4, v**2.5, v)
    else:
        v = ti.max(0., 2 - v)
        col = vec3(v, v**1.5, v**3)
    return col

@ti.kernel
def render():
    for i, j in pixels:
        c = 2.0 * vec2(i, j) / height - vec2(1.8, 1)
        z = vec2(0)
        count = 0
        while count < 100 and dot(z, z) < 50:
            z = cmul(z, z) + c
            count += 1

        if count == 100:
            pixels[i, j] = [0, 0, 0]
        else:
            pixels[i, j] = setcolor(z, count)

render()

from PIL import Image
import IPython

img = Image.fromarray((255 * pixels.to_numpy()).astype('uint8')).transpose(Image.Transpose.TRANSPOSE)
IPython.display.display(img)