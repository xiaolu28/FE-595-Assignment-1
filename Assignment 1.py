#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 20:59:18 2019

@author: xiaolu
"""
import matplotlib.pyplot as plt
import numpy as np
import math 
### create a range from -2*pi to 2 *pi
t = np.linspace(-2 * math.pi, 2 * math.pi, 300)
### plot sine and cosine
plt.plot(t, np.sin(t), label = "Sine")
plt.plot(t, np.cos(t), label = "Cosine")
### create title and legend for graph
plt.title("Graph of sine and cosine")
plt.legend()
plt.xticks((-np.pi*2,-np.pi*3/2,-np.pi,-np.pi/2, 0,
            np.pi/2,np.pi,np.pi*3/2,np.pi*2),
            ('-2π','-3π/2','-π','-π/2','0','π/2','π','3π/2','2π'))

### plot tan(x)
plt.plot(t, np.tan(t), label = "Tan")
### create title and legend for graph
plt.title("Graph of tan")
plt.legend()
