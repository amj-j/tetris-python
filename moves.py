# Moving the current brick left, right and down

from room import down, right, left, remove
from screens import box_height, box_width, grid, block_pos_in_box as block_pos


def is_vacant(x, y): #checks whether a block can be moved to passed coordinates (wheter the place is vacant)
    if x<0 or y<0 or x>=box_width or y>=box_height:
        return False
    #checks whether given position is within the box

    if grid[x][y] != 0:
        return False
    #checks whether given position is not occupied y another existing block
    
    return True


#-----------------------------------------------------------------------------------------
# Checking and clearing full rows if there are any:
#-----------------------------------------------------------------------------------------

def clear_row(y): # deletes all blocks in given row
    for x in range(box_width):
        remove(grid[x][y])
        grid[x][y] = 0

def move_all_above(y_cleared): # moves all blocks above given y one tile down
    for y in reversed(range(y_cleared)):
        for x in range(box_width):
            down(grid[x][y])
            grid[x][y+1] = grid[x][y]
            grid[x][y] = 0

def row_cleaning(): # main function for clearing rows
    rows_cleaned = 0 # number of rows cleaned
    for y in range(box_height): # y - row number
        for x in range(box_width): # x - column number
            if grid[x][y] == 0:
                break
            if x == box_width - 1:
                clear_row(y)
                move_all_above(y)
                rows_cleaned += 1                
    return rows_cleaned

#-----------------------------------------------------------------------------------------
# Moving the brick in lineal directions:
#-----------------------------------------------------------------------------------------

def fall(blocks): #moves whole object one tile down
    for i in blocks:
        x, y = block_pos(i)
        if is_vacant(x, y+1) == False: # if the tile is occupied, the brick blocks will be added to grid
            for j in blocks:
                x_grid, y_grid = block_pos(j)
                grid[x_grid][y_grid] = j
            return True
                
    for i in blocks:
        down(i)
    return False


def go_left(blocks):
    for i in blocks:
        x, y = block_pos(i)
        if is_vacant(x-1, y) == False:
            return
                
    for i in blocks:
        left(i)


def go_right(blocks):
    for i in blocks:
        x, y = block_pos(i)
        if is_vacant(x+1, y) == False:
            return
                
    for i in blocks:
        right(i)