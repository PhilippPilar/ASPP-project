# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:33:24 2021

@author: Philipp Pilar
"""
import numpy as np
import matplotlib.pyplot as plt
import time


#chosen project: The Game of Life

class GameOfLife():
    def __init__(self,state0):
        self.h = state0.shape[0]
        self.w = state0.shape[1]
        self.state0 = state0
        self.state = state0
        
    def update(self):
        state1 = np.zeros([self.h,self.w])
        for i in range(self.h):
            for j in range(self.w):
                v = 0 
                if i != self.h-1:
                    v += self.state[i+1,j]
                if i != 0:
                    v += self.state[i-1,j]
                if j != self.w -1:
                    v += self.state[i,j+1]
                if j != 0:
                    v += self.state[i,j-1]
                
                if v == 2 or v == 2:
                    state1[i,j] = 1
                    
        self.state = state1
    
    def reset(self):
        self.state = self.state0
        
    def evolve(self,N=20):
        for i in range(N):
            plt.imshow(self.state)
            plt.pause(0.0001)
            self.update()

def cross(h,w):
    cross = np.zeros([h,w])
    cross[int(h/2),:] = 1
    cross[:,int(w/2)] = 1
    return cross

def cube(h,w):
    cube = np.zeros([h,w])
    cube[int(3*h/8):int(5*h/8),int(3*w/8):int(5*w/8)] = 1
    #cube[:,int(3*w/8):int(5*w/8)] = 1
    return cube

def checker(h,w):
    c0 = [[1,0],[0,1]]
    checker = np.tile(c0,(int(h/2),int(w/2)))        
    return checker

def random(h,w):
    random = np.random.randint(0,2,h*w).reshape([h,w])
    return random

def stripes(h,w,mode = 0):
    s = np.ones(h-2)
    stripes = np.zeros([h,w])
    stripes += np.diag(s,2) + np.diag(s,-2)
    if mode == 1:
        stripes = np.flip(stripes,0)
    if mode == 2:
        stripes = stripes + np.flip(stripes,0)
    return stripes
    

#%%

#cross
GoL = GameOfLife(cross(16,64))
GoL.evolve(50)

#random
GoL = GameOfLife(random(32,32))
GoL.evolve()

#cube
GoL = GameOfLife(cube(32,32))
GoL.evolve(5)
    
#checkerboard
GoL = GameOfLife(checker(32,32))
GoL.evolve(5)

#stripes
GoL = GameOfLife(stripes(32,32,2))
GoL.evolve(50)
