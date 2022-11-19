# The main file

from screens import create_screen
from game_flow import left_arrow, right_arrow, up_arrow, down_arrow, left_click
from room import root, canvas, initial_settings


#-----------------------------------------------------------------------------------------
# Main:
#-----------------------------------------------------------------------------------------

canvas.pack()
initial_settings()
create_screen("TETRIS", "PLAY", "QUIT")


#-----------------------------------------------------------------------------------------
# Binding arrow keys:
#-----------------------------------------------------------------------------------------

root.bind('<Left>', left_arrow) # moves the brick left
root.bind('<Right>', right_arrow) # moves the brick right
root.bind('<Up>', up_arrow) # rotates the brick clockwise
root.bind('<Down>', down_arrow) # speeds up the downward movement of the brick
root.bind('<Button-1>', left_click) # clicking buttons (play, pause, resume, quit)


root.mainloop()