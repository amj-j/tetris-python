# Creating the screen that will be visible during the game
from room import canvas, block_pos, create_block, canvas_height, canvas_width, remove, east, west, center, text_font

#*****************************************************************************************
# FUNCTIONS AND VARIABLES FOR THE PLAYING SCREEN
#*****************************************************************************************

#-----------------------------------------------------------------------------------------
# Functions and variables related to the box inside which tetris will be played:
#-----------------------------------------------------------------------------------------

box_height = 16 #inner, must be even
box_width = 10 #inner, must be even

offset_left = 1
offset_up = 1
# offset from upper left corner

grid = [] # grid is a list of lists (matrix) of all the block tiles within the box 

box_center = int(offset_left + 1 + box_width/2) # the first block to the right of the horizontal center of the box

def block_pos_in_box(block):
    x, y = block_pos(block)
    x -= offset_left+1
    y -= offset_up
    return x, y

def walls():
    for i in range(box_height + 1):
        create_block(offset_left, offset_up+i, "#C3C3C3")
        create_block(offset_left+box_width+1, offset_up+i, "#C3C3C3")

def bottom():
    for i in range(box_width):
        create_block(offset_left+i+1, offset_up+box_height, "#C3C3C3")

def create_grid():
    for i in range(box_width):
        grid.append([])
        for j in range(box_height):
            grid[i].append(0)

def reset_grid():
    for x in range(box_width):
        for y in range(box_height):
            if grid[x][y] != 0:
                remove(grid[x][y])
                grid[x][y] = 0

#-----------------------------------------------------------------------------------------
# Functions and variables related to rest of the game screen (widgets like pause button and scoreboard):
#-----------------------------------------------------------------------------------------

score_text = 0 # canvas.create_text() will be stored here

widgets_x0 = (offset_left+box_width+3)*30 # x coordinate where widgets begin
widgets_x1 = (offset_left+box_width+11)*30 # x coordinate where widgets end
y_slice = int(canvas_height/24) # y axis is sliced so that symetry is easier
pause_button_coords = [widgets_x0, y_slice*10, widgets_x1, y_slice*12]


def pause_button(): 
    canvas.create_rectangle(pause_button_coords, width = 5,  fill = "#66A5DD")
    x_text = int((pause_button_coords[2]+pause_button_coords[0])/2)
    y_text = int((pause_button_coords[3]+pause_button_coords[1])/2)
    canvas.create_text(x_text, y_text, text = "PAUSE", font = text_font)

def scoreboard():
    x0, y0 = widgets_x0, y_slice*7
    x1, y1 = widgets_x1, y_slice*9
    canvas.create_rectangle(x0, y0, x1, y1, width = 5,  fill = "#FFFFFF")
    canvas.create_text(widgets_x0+10, int((y0+y1)/2), text = "SCORE:", font = text_font, anchor = west)

def score_print(score):
    global score_text
    if score_text != 0:
        canvas.delete(score_text)
    score_text = canvas.create_text(widgets_x1-10, int((y_slice*7+y_slice*9)/2), text = score, font = text_font, anchor = east)




#*****************************************************************************************
# FUNCTIONS AND VARIABLEC FOR OTHER SCREENS
#*****************************************************************************************

objects = [0, 0, 0, 0, 0, 0] # Storage for the objects that make the non-playing screen

# Coordinates of the buttons in the non-playing screen
buttons_x0 = int(canvas_width/8)*3
button1_y0 = int(canvas_height/24)*7
button2_y0 = int(canvas_height/24)*10
buttons_x1 = int(canvas_width/8)*5
button1_y1 = int(canvas_height/24)*9
button2_y1 = int(canvas_height/24)*12


def create_screen(title, first_button, second_button): # Creating the objects that make the non-playing screen
    objects[0] = canvas.create_rectangle(0, 0, canvas_width, canvas_height,  fill = "#FFFFC5") # screen background
    objects[1] = canvas.create_text(int(canvas_width/2), int(canvas_height/24)*5, text = title, font = text_font, justify = center) # title
    objects[2] = canvas.create_rectangle(buttons_x0, button1_y0, buttons_x1, button1_y1, width = 5,  fill = "#6FDD66") # first button
    objects[3] = canvas.create_rectangle(buttons_x0, button2_y0, buttons_x1, button2_y1, width = 5,  fill = "#FF3E3E") # second button
    objects[4] = canvas.create_text(int(canvas_width/2), int(canvas_height/24)*8, text = first_button, font = text_font) # first button text
    objects[5] = canvas.create_text(int(canvas_width/2), int(canvas_height/24)*11, text = second_button, font = text_font) # second button text


def remove_screen(): # Deleting the objects that make the non-playing screen
    global objects
    for i in objects:
        canvas.delete(i)