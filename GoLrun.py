# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:33:24 2021

@author: Philipp Pilar
"""

import GameOfLife.gameoflife as GoL
import GameOfLife.patterns as pt

import numpy as np
import time


#chosen project: The Game of Life
#%%

#cross
print('cross')
G1 = GoL.GameOfLife(pt.cross(32,32))
G1.evolve(100,plot='gif',name='cross')

#%%
#random
print('random')
G2 = GoL.GameOfLife(pt.random(50,50))
G2.evolve(100,plot='gif',name='random')


# #create data for test file
# state0 = G2.state0
# state1 = G2.state
# np.savetxt('state0.txt',state0)
# np.savetxt('state1.txt',state1)


#%%
#cube
print('cube')
G3 = GoL.GameOfLife(pt.cube(32,32))
G3.evolve(300,plot='gif',name='cube')
    
#checkerboard
print('checkerboard')
G4 = GoL.GameOfLife(pt.checker(32,32))
G4.evolve(300,plot='gif',name='checkerboard')
#%%
#stripes
print('stripes')
G5 = GoL.GameOfLife(pt.stripes(100,100,2))
G5.evolve(600,plot='gif',name='stripes')
#%%
#glider
print('glider')
G6 = GoL.GameOfLife(pt.glider(16,16))
G6.evolve(55,plot='gif',name='glider')
G6.gif('glider')
