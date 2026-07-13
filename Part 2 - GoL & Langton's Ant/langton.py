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
    """
    TODO: [Part 2 - Langton's Ant]
    Create the LangtonsAnt class.
    
    Instruct students to:
    1. Implement the core rules:
       - If on a white square, toggle the color of the square and turn 90 degrees clockwise ('R'), then move forward one unit.
       - If on a black square, toggle the color of the square and turn 90 degrees counter-clockwise ('L'), then move forward one unit.
    2. Extend it to handle multi-color states (representing rulesets like RLR, LLRR, LRRRRRLLR, etc.).
       - A ruleset dictionary maps: {current_color: (next_color, turn_direction)}
       - Where turn_direction is 'R' or 'L'.
    3. Ensure wrapping at the boundaries (toroidal grid).
    """



    def __init__(self, N, ant_position, rules):
        """
        Initialize the Langton's Ant simulation.
        
        Args:
            N (int): The grid size (NxN).
            ant_position (tuple): Starting coordinate of the ant as (r, c).
            rules (dict): Dictionary defining transition rules.
                          Format: {current_color: (next_color, turn_direction)}
        """
        # Student TODO: Implement initialization
        self.grid = np.zeros((N,N), np.uint)
        self.N = N
        self.r , self.c =ant_position
        self.rules = rules 
        self.direction = Direction.North

    def get_states(self):
        """
        Returns the current state grid of the cells.
        
        Returns:
            np.ndarray: The NxN cellular grid.
        """
        # Student TODO: Return grid state
        return self.grid

    def get_current_position(self):
        """
        Returns the ant's current position as a tuple (r, c).
        
        Returns:
            tuple: Current coordinates of the ant.
        """
        # Student TODO: Return current position
        return (self.r , self.c)

    def step(self):
        """
        Perform a single simulation step following the ruleset.
        """
        # Student TODO: Implement the ant's movement and cell state updates
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
