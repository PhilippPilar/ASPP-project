# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:33:24 2021

@author: Philipp Pilar
"""
import numpy as np
import matplotlib.pyplot as plt
import time


#chosen project: The Game of Life


#create initial pattern
lh = 32
lw = 32
state0 = np.zeros([lh,lw])
state0[int(lh/2),:] = 1
state0[:,int(lw/2)] = 1

#plot
plt.imshow(state0)

def update_state(state0):
    state1 = np.zeros(state0.shape)
    for i in range(state0.shape[0]):
        for j in range(state0.shape[1]):
            v = 0 
            if i != state0.shape[0]-1:
                v += state0[i+1,j]
            if i != 0:
                v += state0[i-1,j]
            if j != state0.shape[1]-1:
                v += state0[i,j+1]
            if j != 0:
                v += state0[i,j-1]
            
            if v == 2 or v == 2:
                state1[i,j] = 1
            
    return state1


for j in range(78):
    print(j)
    state1 = update_state(state0)
    plt.imshow(state1)
    plt.pause(0.0001)
    time.sleep(0.1)
    state0 = state1