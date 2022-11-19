# Picking and creating the brick which will go next

# brick is a list containing:
    # touple of four blocks [0]
    # string identifier [1]
    # rotation position [2]


from random import choice
from room import create_block
from screens import offset_up, box_center


def pick_a_brick():
    rand = choice(["orange", "red", "yellow", "blue", "purple", "lime", "sky_blue"])
    if rand == "orange":
        brick = create_orange()
    elif rand == "red":
        brick = create_red()
    elif rand == "yellow":
        brick = create_yellow()
    elif rand == "blue":
        brick = create_blue()
    elif rand == "purple":
        brick = create_purple()
    elif rand == "lime":
        brick = create_lime()
    elif rand == "sky_blue":
        brick = create_sky_blue()
    return brick


def create_orange():
    a = create_block(box_center-2, offset_up, "orange")
    b = create_block(box_center-1, offset_up, "orange")
    c = create_block(box_center, offset_up, "orange")
    d = create_block(box_center+1, offset_up, "orange")
    return [[a, b, c, d], "orange", 0]

def create_red():
    a = create_block(box_center-1, offset_up, "red")
    b = create_block(box_center, offset_up, "red")
    c = create_block(box_center-1, offset_up+1, "red")
    d = create_block(box_center, offset_up+1, "red")
    return [[a, b, c, d,], "red", 0]

def create_yellow():
    a = create_block(box_center-2, offset_up, "yellow")
    b = create_block(box_center-1, offset_up, "yellow")
    c = create_block(box_center, offset_up, "yellow")
    d = create_block(box_center-1, offset_up+1, "yellow")
    return [[a, b, c, d], "yellow", 0]

def create_blue():
    a = create_block(box_center-2, offset_up, "blue")
    b = create_block(box_center-1, offset_up, "blue")
    c = create_block(box_center, offset_up, "blue")
    d = create_block(box_center-2, offset_up+1, "blue")
    return [[a, b, c, d], "blue", 0]

def create_purple():
    a = create_block(box_center-2, offset_up, "purple")
    b = create_block(box_center-1, offset_up, "purple")
    c = create_block(box_center, offset_up, "purple")
    d = create_block(box_center, offset_up+1, "purple")
    return [[a, b, c, d], "purple", 0]

def create_lime():
    a = create_block(box_center-2, offset_up, "lime")
    b = create_block(box_center-1, offset_up, "lime")
    c = create_block(box_center-1, offset_up+1, "lime")
    d = create_block(box_center, offset_up+1, "lime")
    return [[a, b, c, d], "lime", 0]

def create_sky_blue():
    a = create_block(box_center-2, offset_up+1, "SkyBlue1")
    b = create_block(box_center-1, offset_up, "SkyBlue1")
    c = create_block(box_center-1, offset_up+1, "SkyBlue1")
    d = create_block(box_center, offset_up, "SkyBlue1")
    return [[a, b, c, d], "sky_blue", 0]
