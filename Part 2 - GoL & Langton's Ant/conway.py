"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

"""
import numpy as np
from scipy import signal, ndimage
from scipy.signal import convolve2d


import re

def parse_rle(filepath):

    width = height = 0
    live_cells = []
    data_lines = []
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith('#'):
                continue
            if line.startswith('x ='):
                match = re.search(r'x\s*=\s*(\d+)\s*,\s*y\s*=\s*(\d+)', line)
                if match:
                    width, height = map(int, match.groups())
                continue
            data_lines.append(line)
    
    data = ''.join(data_lines)

    if width == 0 or height == 0:
        raise ValueError("Invalid RLE file: missing header")
    row = 0
    col = 0
    run_length = 0
    i = 0
    while i < len(data):
        ch = data[i]
        if ch.isdigit():
            run_length = 0
            while i < len(data) and data[i].isdigit():
                run_length = run_length * 10 + int(data[i])
                i += 1
            continue  
        
        if ch == 'o':
            if run_length == 0:
                run_length = 1
            for _ in range(run_length):
                live_cells.append((row, col))
                col += 1
            run_length = 0
        
        elif ch == 'b':
            if run_length == 0:
                run_length = 1
            col += run_length
            run_length = 0
    
        elif ch == '$':
            if run_length == 0:
                run_length = 1
            row += run_length
            col = 0
            run_length = 0
        
        elif ch == '!':
            break
        
        i += 1
    print(width , height)
    print(len(live_cells))
    for l in live_cells:
        print(l)
    return width, height, live_cells

def parse_pattern(filepath):

    if filepath.endswith('.cells'):
        return parse_plaintext(filepath)  
    elif filepath.endswith('.rle'):
        return parse_rle(filepath)
    else:
        raise ValueError("Unsupported file format. Use .cells or .rle")

def parse_plaintext(filepath):
    width = 0 
    r=0
    live_cells = []
    with open(filepath, 'r', encoding='utf-8-sig') as file:
        for line in file:
            valid_line = line
            if not valid_line or valid_line.startswith('!'):
                continue

            if len(valid_line)>width:
                width= len(valid_line)
            
            for c,char in enumerate(valid_line):
                if char=='O' or char == '':
                    live_cells.append((r,c))
            r+=1
    height = r

    print(width , height)
    print(len(live_cells))
    for l in live_cells:
        print(l)

    return (width , height , live_cells)


class GameOfLife:

    def __init__(self, N=256, finite=True, fastMode=True):
        self.grid = np.zeros((N, N), np.uint)
        self.neighborhood = np.ones((3, 3), np.uint)  # 8 connected kernel
        self.neighborhood[1, 1] = 0  # do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.rows = N  # use for slow implementation of evolve
        self.cols = N  # use for slow implementation of evolve

    def getStates(self):

        return self.grid

    def getGrid(self):

        return self.getStates()

    def update_grid_fast(self, grid):
        if self.finite:
            neighborC=convolve2d(self.grid , self.neighborhood , mode='same' , boundary='fill', fillvalue=0)
        else:
            neighborC=convolve2d(self.grid , self.neighborhood , mode='same' , boundary='wrap')
        
        checking_aliveValue = (self.grid== self.aliveValue)
        new_grid = (neighborC==3) | (checking_aliveValue & (neighborC==2))
        self.grid=np.where(new_grid ,self.aliveValue,self.deadValue).astype(self.grid.dtype)
        return self.grid

    def evolve(self):

        if self.fastMode:
            self.grid = self.update_grid_fast(self.grid)
        else:
            N= self.rows 
            new_grid =np.zeros((N, N),dtype= self.grid.dtype)
            neighbors = [-1, 0 , 1]
            for r in range(N):
                for c in range(N):
                    nCount=0
                    for i in neighbors:
                        for j in neighbors:
                            if i==0 and j==0 :
                                continue
                            nr = r+i
                            nc= c+j
                            if not self.finite:
                                if nr<0:
                                    nr = self.rows-1
                                if nr>=self.rows:
                                    nr =0
                                if nc<0:
                                    nc= self.cols-1
                                if nc>=self.cols:
                                    nc=0
                            if 0<=nr<self.rows and 0<=nc <self.cols:
                                if self.grid[nr,nc]== self.aliveValue:
                                    nCount+=1              
                    if self.grid[r,c]==self.aliveValue:
                        if nCount<2 or nCount>3 :
                            new_grid[r,c]=self.deadValue
                        if nCount==2 or nCount==3:
                            new_grid[r,c]=self.aliveValue
                    else:
                        if nCount==3:
                            new_grid[r,c]=self.aliveValue
                        else:
                            new_grid[r,c]=self.deadValue
            self.grid= new_grid
            print(f"Population: {np.sum(self.grid)}")

    def insertBlinker(self, index=(0, 0)):

        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue

    def insertGlider(self, index=(0, 0)):

        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 2, index[1]] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 2] = self.aliveValue

    def insertGliderGun(self, index=(0, 0)):

        self.grid[index[0] + 1, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 2, index[1] + 24] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 3, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 15] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 36] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 37] = self.aliveValue

        self.grid[index[0] + 4, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 36] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 37] = self.aliveValue

        self.grid[index[0] + 5, index[1] + 1 + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 2 + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 23] = self.aliveValue

        self.grid[index[0] + 6, index[1] + 1 + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 2 + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 16] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 19] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 24] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 26] = self.aliveValue



        self.grid[index[0] + 7, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 8, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 8, index[1] + 17] = self.aliveValue

        self.grid[index[0] + 9, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 9, index[1] + 15] = self.aliveValue

    def insertFromFile(self, filename, index=((0, 0))):

        width, height, live_cells = parse_pattern(filename)
        for r, c in live_cells:
            target_r = index[0] + r
            target_c = index[1] + c
            if 0 <= target_r < self.rows and 0 <= target_c < self.cols:
                self.grid[target_r, target_c] = self.aliveValue
