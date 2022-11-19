# Rotating the current brick

from room import movexy
from screens import box_height, box_width, grid, block_pos_in_box as block_pos

def choose_rotation(brick):
    if brick[1] == "orange":
        rotate_orange(brick)
    elif brick[1] == "yellow":
        rotate_yellow(brick)
    elif brick[1] == "blue":
        rotate_blue(brick)
    elif brick[1] == "purple":
        rotate_purple(brick)
    elif brick[1] == "lime":
        rotate_lime(brick)
    elif brick[1] == "sky_blue":
        rotate_sky_blue(brick)
    

def check_area(x0, y0, xn, yn): # checks whether the area around the brick is free so that it can rotate
    if x0<0 or y0<0 or xn>=box_width or yn>=box_height:
        return False
    #checks whether given position is within the box
    
    for x in range(x0, xn+1):
        for y in range(y0, yn+1):
            if grid[x][y] != 0:
                return False
    #checks whether given position is not occupied y another existing block

    return True

# There is no pattern in rotating different blocks to different positions,
# so in the next part all rotations are brute-forced.
# You can find reference guide in positions.txt

def rotate_orange(brick):

    def to_pos0(blocks):
        movexy(blocks[0], -1, 1)
        movexy(blocks[2], 1, -1)
        movexy(blocks[3], 2, -2)

    def to_pos1(blocks):
        movexy(blocks[0], 1, -1)
        movexy(blocks[2], -1, 1)
        movexy(blocks[3], -2, 2)
    
    x0, y0 = block_pos(brick[0][1]) # coordinations of the second block of the brick (it's always in the centre)
    if check_area(x0-1, y0-1, x0+2, y0+2): # 4x4 area
        if brick[2] == 0:
            to_pos1(brick[0])
            brick[2] = 1
        elif brick[2] == 1:
            to_pos0(brick[0])
            brick[2] = 0


def rotate_yellow(brick):

    def to_pos0(blocks):
        movexy(blocks[0], -1, -1)
        movexy(blocks[2], 1, 1)
        movexy(blocks[3], -1, 1)
    
    def to_pos1(blocks):
        movexy(blocks[2], -1, -1)
    
    def to_pos2(blocks):
        movexy(blocks[3], 1, -1)
    
    def to_pos3(blocks):
        movexy(blocks[0], 1, 1)

    x0, y0 = block_pos(brick[0][1]) # coordinations of the second block of the brick (it's always in the centre)
    if check_area(x0-1, y0-1, x0+1, y0+1):
        if brick[2] == 0:
            to_pos1(brick[0])
            brick[2] = 1
        elif brick[2] == 1:
            to_pos2(brick[0])
            brick[2] = 2
        elif brick[2] == 2:
            to_pos3(brick[0])
            brick[2] = 3
        elif brick[2] == 3:
            to_pos0(brick[0])
            brick[2] = 0


def rotate_blue(brick):

    def to_pos0(blocks):
        movexy(blocks[0], -1, -1)
        movexy(blocks[2], 1, 1)
        movexy(blocks[3], -2, 0)
    
    def to_pos1(blocks):
        movexy(blocks[0], 1, -1)
        movexy(blocks[2], -1, 1)
        movexy(blocks[3], 0, -2)
    
    def to_pos2(blocks):
        movexy(blocks[0], 1, 1)
        movexy(blocks[2], -1, -1)
        movexy(blocks[3], 2, 0)
    
    def to_pos3(blocks):
        movexy(blocks[0], -1, 1)
        movexy(blocks[2], 1, -1)
        movexy(blocks[3], 0, 2)
    
    x0, y0 = block_pos(brick[0][1]) # coordinations of the second block of the brick (it's always in the centre)
    if check_area(x0-1, y0-1, x0+1, y0+1): # 3x3 area
        if brick[2] == 0:
            to_pos1(brick[0])
            brick[2] = 1
        elif brick[2] == 1:
            to_pos2(brick[0])
            brick[2] = 2
        elif brick[2] == 2:
            to_pos3(brick[0])
            brick[2] = 3
        elif brick[2] == 3:
            to_pos0(brick[0])
            brick[2] = 0


def rotate_purple(brick):

    def to_pos0(blocks):
        movexy(blocks[0], -1, -1)
        movexy(blocks[2], 1, 1)
        movexy(blocks[3], 0, 2)
    
    def to_pos1(blocks):
        movexy(blocks[0], 1, -1)
        movexy(blocks[2], -1, 1)
        movexy(blocks[3], -2, 0)
    
    def to_pos2(blocks):
        movexy(blocks[0], 1, 1)
        movexy(blocks[2], -1, -1)
        movexy(blocks[3], 0, -2)
    
    def to_pos3(blocks):
        movexy(blocks[0], -1, 1)
        movexy(blocks[2], 1, -1)
        movexy(blocks[3], 2, 0)
    
    x0, y0 = block_pos(brick[0][1]) # coordinations of the second block of the brick (it's always in the centre)
    if check_area(x0-1, y0-1, x0+1, y0+1): # 3x3 area
        if brick[2] == 0:
            to_pos1(brick[0])
            brick[2] = 1
        elif brick[2] == 1:
            to_pos2(brick[0])
            brick[2] = 2
        elif brick[2] == 2:
            to_pos3(brick[0])
            brick[2] = 3
        elif brick[2] == 3:
            to_pos0(brick[0])
            brick[2] = 0


def rotate_lime(brick):

    def to_pos0(blocks):
        movexy(blocks[0], -1, 1)
        movexy(blocks[2], 1, 1)
        movexy(blocks[3], 2, 0)

    def to_pos1(blocks):
        movexy(blocks[0], 1, -1)
        movexy(blocks[2], -1, -1)
        movexy(blocks[3], -2, 0)
    
    x0, y0 = block_pos(brick[0][1]) # coordinations of the second block of the brick (it's always in the centre)
    if check_area(x0-1, y0-1, x0+1, y0+1): # 3x3 area
        if brick[2] == 0:
            to_pos1(brick[0])
            brick[2] = 1
        elif brick[2] == 1:
            to_pos0(brick[0])
            brick[2] = 0


def rotate_sky_blue(brick):

    def to_pos0(blocks):
        movexy(blocks[0], -2, 0)
        movexy(blocks[2], -1, 1)
        movexy(blocks[3], 1, 1)

    def to_pos1(blocks):
        movexy(blocks[0], 2, 0)
        movexy(blocks[2], 1, -1)
        movexy(blocks[3], -1, -1)
    
    x0, y0 = block_pos(brick[0][1]) # coordinations of the second block of the brick (it's always in the centre)
    if check_area(x0-1, y0-1, x0+1, y0+1): # 3x3 area
        if brick[2] == 0:
            to_pos1(brick[0])
            brick[2] = 1
        elif brick[2] == 1:
            to_pos0(brick[0])
            brick[2] = 0