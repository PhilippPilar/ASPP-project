# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:33:24 2021

@author: Philipp Pilar
"""

import gameoflife.gameoflife as GoL
import gameoflife.patterns as pt


#chosen project: The Game of Life
#%%

#cross
print('cross')
G1 = GoL.GameOfLife(pt.cross(32,32))
G1.evolve(100)
G1.gif('cross')

#%%
#random
print('random')
G2 = GoL.GameOfLife(pt.random(128,128))
G2.evolve(700)
G2.gif('random')

#%%
#cube
print('cube')
G3 = GoL.GameOfLife(pt.cube(32,32))
G3.evolve(300)
G3.gif('cube')
    
#checkerboard
print('checkerboard')
G4 = GoL.GameOfLife(pt.checker(32,32))
G4.evolve(300)
G4.gif('checkerboard')
#%%
#stripes
print('stripes')
G5 = GoL.GameOfLife(pt.stripes(100,100,2))
G5.evolve(600)
G5.gif('stripes')
#%%
#glider
print('glider')
G6 = GoL.GameOfLife(pt.glider(16,16))
G6.evolve(55)
G6.gif('glider')
