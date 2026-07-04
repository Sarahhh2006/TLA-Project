
import numpy as np 

glinder_gun = ([
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
])
true_grid = np.zeros((15,45))
true_grid[1:10 , 1:37] = glinder_gun

original_grid = np.zeros((15,45))
index = (0,0)
original_grid[index[0] + 1, index[1] + 26] =1
original_grid[index[0] + 2, index[1] + 24] = 1
original_grid[index[0] + 2, index[1] + 26] = 1
original_grid[index[0] + 3, index[1] + 14] = 1
original_grid[index[0] + 3, index[1] + 15] = 1
original_grid[index[0] + 3, index[1] + 22] = 1
original_grid[index[0] + 3, index[1] + 23] = 1
original_grid[index[0] + 3, index[1] + 36] = 1
original_grid[index[0] + 3, index[1] + 37] = 1
original_grid[index[0] + 4, index[1] + 13] = 1
original_grid[index[0] + 4, index[1] + 17] = 1
original_grid[index[0] + 4, index[1] + 22] = 1
original_grid[index[0] + 4, index[1] + 23] = 1
original_grid[index[0] + 4, index[1] + 36] = 1
original_grid[index[0] + 4, index[1] + 37] = 1
original_grid[index[0] + 5, index[1] + 1 + 1] = 1
original_grid[index[0] + 5, index[1] + 2 + 1] = 1
original_grid[index[0] + 5, index[1] + 12] = 1
original_grid[index[0] + 5, index[1] + 18] = 1
original_grid[index[0] + 5, index[1] + 22] = 1
original_grid[index[0] + 5, index[1] + 23] = 1
original_grid[index[0] + 6, index[1] + 1 + 1] = 1
original_grid[index[0] + 6, index[1] + 2 + 1] = 1
original_grid[index[0] + 6, index[1] + 12] = 1
original_grid[index[0] + 6, index[1] + 16] = 1
original_grid[index[0] + 6, index[1] + 18] = 1
original_grid[index[0] + 6, index[1] + 19] = 1
original_grid[index[0] + 6, index[1] + 24] = 1
original_grid[index[0] + 6, index[1] + 26] = 1
original_grid[index[0] + 7, index[1] + 12] = 1
original_grid[index[0] + 7, index[1] + 18] = 1
original_grid[index[0] + 7, index[1] + 26] = 1
original_grid[index[0] + 8, index[1] + 13] = 1
original_grid[index[0] + 8, index[1] + 17] = 1
original_grid[index[0] + 9, index[1] + 14] = 1
original_grid[index[0] + 9, index[1] + 15] = 1

diff = original_grid- true_grid
mismatch= np.argwhere(diff!=0)
if len(mismatch)!=0:
    print(f"found {len(mismatch)} differences")
    for row ,col in mismatch:
        val =diff[row,col]
        if val>0 :
            stat = "delete"
        stat = "add"
        print(f"row:{row} col:{col} -> {stat}")