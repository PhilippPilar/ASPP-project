# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:51:08 2021

@author: Philipp Pilar
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter
import time


class GameOfLife():
    """
    Class keeping track of the state(s) of an instance of the game of life.
    
    Methods
    -------
    
    update:
        update state according to rules
    reset:
        reset to initial state
    evolve:
        evolve GoL for N steps
    gif:
        create gif of evoultion
    
    """
    def __init__(self,state0):
        """
        Initializes a GameOfLife with initial state state0.
        
        Parameters
        ----------
        state0 : int, 2D-array
        
        """
        self.h = state0.shape[0]
        self.w = state0.shape[1]
        self.state0 = state0
        self.state = state0
        self.ims = []
      
        
    def update(self):
        """
        Updates the state of the GoL according to the game rules.
        
        """
        buf = np.zeros([self.h+2,self.w+2])
        buf[1:self.h+1,1:self.w+1] = self.state
        state1 = np.zeros([self.h,self.w])
        for i in range(1,self.h+1):
            for j in range(1,self.w+1):
                v = 0
                v += np.sum(buf[i+1,j-1:j+2])
                v += buf[i,j-1] + buf[i,j+1]
                v += np.sum(buf[i-1,j-1:j+2])
                
                if self.state[i-1,j-1] == 0:
                    if v == 3:
                        state1[i-1,j-1] = 1
                else:
                    if v == 2 or v == 3:
                        state1[i-1,j-1] = 1
                    
        self.state = state1
        
    
    def reset(self):
        """
        Resets the state of the GoL to its initial state.
        
        """
        self.state = self.state0
        self.ims = []
        
    def evolve(self,N=20):
        """
        Evolve the GoL for N steps.
        
        Parameters
        ----------
        N : int
        
        """
        self.fig = plt.figure()#figsize = (min(self.h/5,50),min(self.w/5,50)))
        for i in range(N):
            im = plt.imshow(self.state)#,cmap='cividis')
            plt.axis('off')
            self.ims.append([im])
            plt.pause(0.0001)
            self.update()
        
    def gif(self,name):
        """
        Saves a name.gif as visualization of the evolution of the GoL.
        
        Parameters
        ----------
        name : str
               name of gif
        
        """
        #fig = plt.figure()
        ani = animation.ArtistAnimation(self.fig,self.ims,interval=50,blit=True,repeat_delay=500)
        writer = PillowWriter(fps=10)
        ani.save(name+'.gif',writer = writer)
        plt.show()