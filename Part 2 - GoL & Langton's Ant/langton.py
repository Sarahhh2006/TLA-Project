# -*- coding: utf-8 -*-
"""
Langton's Ant Student Template Module.

"""
import numpy as np
from enum import IntEnum
class Direction(IntEnum):
    North= 0
    East= 1
    South= 2
    West= 3

class LangtonsAnt:

    def __init__(self, N, ant_position, rules):
        self.grid = np.zeros((N,N), np.uint)
        self.N = N
        self.r , self.c =ant_position
        self.rules = rules 
        self.direction = Direction.North


    def get_states(self):
       return self.grid

    def get_current_position(self):
        return (self.r , self.c)

    def step(self):
        curr_color = self.grid[self.r, self.c]
        next_color , turn_direction = self.rules[curr_color]
        self.grid[self.r , self.c]= next_color

        if turn_direction=='R':
            self.direction = Direction((self.direction+1)%4)
        else:
            self.direction = Direction((self.direction-1)%4)

        if self.direction == Direction.North:
            self.r-=1
        elif self.direction ==Direction.East:
            self.c +=1
        elif self.direction == Direction.South:
            self.r+=1
        elif self.direction == Direction.West:
            self.c -=1

        if self.r<0:
            self.r = self.N-1
        elif self.r >= self.N:
            self.r = 0 
        
        if self.c <0 :
            self.c = self.N-1
        elif self.c >= self.N:
            self.c= 0 



    def update(self):
        """
        Alias for step() to support standard animation.
        """
        self.step()
