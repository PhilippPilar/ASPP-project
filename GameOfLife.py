# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:33:24 2021

@author: Philipp Pilar
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import time


#chosen project: The Game of Life

class GameOfLife():
    def __init__(self,state0):
        self.h = state0.shape[0]
        self.w = state0.shape[1]
        self.state0 = state0
        self.state = state0
        self.ims = []
        
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
        self.ims = []
        
    def evolve(self,N=20):
        self.fig = plt.figure()
        for i in range(N):
            im = plt.imshow(self.state)
            self.ims.append([im])
            #plt.pause(0.0001)
            self.update()
        
    def gif(self,name):
        #fig = plt.figure()
        ani = animation.ArtistAnimation(self.fig,self.ims,interval=50,blit=True,repeat_delay=500)
        writer = PillowWriter(fps=10)
        ani.save(name+'.gif',writer = writer)
        plt.show()
        
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
print('cross')
GoL = GameOfLife(cross(16,64))
GoL.evolve(30)
GoL.gif('cross')

#random
print('random')
GoL = GameOfLife(random(32,32))
GoL.evolve(25)
GoL.gif('random')

# #cube
#print('cube')
# GoL = GameOfLife(cube(32,32))
# GoL.evolve(5)
    
# #checkerboard
#print('checkerboard')
# GoL = GameOfLife(checker(32,32))
# GoL.evolve(5)

#stripes
print('stripes')
GoL = GameOfLife(stripes(100,100,2))
GoL.evolve(120)
GoL.gif('stripes')
