# -*- coding: utf-8 -*-
"""
Glider-based Logic Gates Student Template Module.

"""
import numpy as np
from conway import GameOfLife
from pygame_viewer import run_pygame_life

CELL_SCALE = 10




class GliderLogicGates:


    def setup_and_gate(self, input_a_present=False, input_b_present=False, grid_size=35):
        N=grid_size
        life = GameOfLife(N)
        
        if input_a_present:
            r, c = 4, 2
            life.grid[r,     c + 1] = life.aliveValue
            life.grid[r + 1, c + 2] = life.aliveValue
            life.grid[r + 2, c]     = life.aliveValue
            life.grid[r + 2, c + 1] = life.aliveValue
            life.grid[r + 2, c + 2] = life.aliveValue

        if input_b_present:  
            r, c = 1, 23
            life.grid[r,     c + 1] = life.aliveValue
            life.grid[r + 1, c]     = life.aliveValue
            life.grid[r + 2, c]     = life.aliveValue
            life.grid[r + 2, c + 1] = life.aliveValue
            life.grid[r + 2, c + 2] = life.aliveValue
        return life
    def setup_not_gate(self, input_a_present=False, grid_size=35):
        N=grid_size
        life = GameOfLife(N)
        
        if input_a_present:
            r, c =2, 1
            life.grid[r,     c + 1] = life.aliveValue
            life.grid[r + 1, c + 2] = life.aliveValue
            life.grid[r + 2, c]     = life.aliveValue
            life.grid[r + 2, c + 1] = life.aliveValue
            life.grid[r + 2, c + 2] = life.aliveValue


        r, c = 1, 23
        life.grid[r,     c + 1] = life.aliveValue
        life.grid[r + 1, c]     = life.aliveValue
        life.grid[r + 2, c]     = life.aliveValue
        life.grid[r + 2, c + 1] = life.aliveValue
        life.grid[r + 2, c + 2] = life.aliveValue
        return life

    def run_and_gate(self, input_a_present, input_b_present):

        gates=self.setup_and_gate( input_a_present, input_b_present)
        # run_pygame_life(gates, cell_scale=CELL_SCALE, fps=8, max_frames=60, title="Game of Life - Glider Check")
        for i in range(60):
            gates.evolve()
        if gates.grid[15,12]==1:
            return True
        else:
            return False

    def run_not_gate(self, input_a_present):
        gates=self.setup_not_gate( input_a_present)
        # run_pygame_life(gates, cell_scale=CELL_SCALE, fps=8, max_frames=60, title="Game of Life - Glider Check")
        for i in range(60):
            gates.evolve()
        alive = np.count_nonzero(gates.grid)
        if  alive == 0  :
            return False 
        else:
            return True

    # def setup_not_gate2(self, input_a_present=False, input_b_present=False, grid_size=35):
    #     N=grid_size
    #     life = GameOfLife(N)
        
    #     if input_a_present:
    #         r, c =2, 1
    #         life.grid[r,     c + 1] = life.aliveValue
    #         life.grid[r + 1, c + 2] = life.aliveValue
    #         life.grid[r + 2, c]     = life.aliveValue
    #         life.grid[r + 2, c + 1] = life.aliveValue
    #         life.grid[r + 2, c + 2] = life.aliveValue

    #     if input_b_present:
    #         r, c = 1, 23
    #         life.grid[r,     c + 1] = life.aliveValue
    #         life.grid[r + 1, c]     = life.aliveValue
    #         life.grid[r + 2, c]     = life.aliveValue
    #         life.grid[r + 2, c + 1] = life.aliveValue
    #         life.grid[r + 2, c + 2] = life.aliveValue
    #     return life


    # def run_not_gate2(self, input_a_present, input_b_present):
    #     gates=self.setup_not_gate2( input_a_present, input_b_present)
    #     #run_pygame_life(gates, cell_scale=CELL_SCALE, fps=8, max_frames=60, title="Game of Life - Glider Check")
    #     for i in range(60):
    #         gates.evolve()
    #     alive = np.count_nonzero(gates.grid)
    #     if alive==0:
    #         return False  
    #     else:
    #         return True

def main():
    """Run the dragon spaceship demo in pygame."""
    logic = GliderLogicGates()

    print("True and True =")
    print(logic.run_and_gate(True,True))
    print("False and True =")
    print(logic.run_and_gate(False,True))
    print("True and False =")
    print(logic.run_and_gate(True,False))
    print("Fasle and False =")
    print(logic.run_and_gate(False,False))

    print()

    print("A=True  -> A'= " )
    print(logic.run_not_gate(True))
    print("A=False  -> A'= " )
    print(logic.run_not_gate(False))


    # print(logic.run_not_gate2(True,False))
    # print(logic.run_not_gate2(False,False))
    # print(logic.run_not_gate2(True,True))
    # print(logic.run_not_gate2(False,True))




if __name__ == "__main__":
    main()