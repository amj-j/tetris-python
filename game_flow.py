# Functions that make the gameloop

import screens
from bricks import pick_a_brick
from moves import fall, row_cleaning, go_left, go_right
from room import root, canvas
from rotations import choose_rotation

score = 0
brick = pick_a_brick()
game_status = 0 # 0 = first menu, 1 = playing game, 2 = paused, 3 = game over

def end():
    # if any block in two upper rows is filled with a fallen block, function returns True and the game ends
    for x in range(screens.box_width):
        for y in range(2):
            if screens.grid[x][y] != 0:
                return True
    return False

def step(): # moving the falling brick down and creating a new one if it reaches the ground
    global brick
    global score
    global game_status
    next = fall(brick[0])
    if next == True: # if the brick has already hit the ground and new brick is to be created
        score_tmp = score
        score += row_cleaning() #score is number of rows that have been cleaned
        if score != score_tmp:
            screens.score_print(score)
        if end() == True:
            return False
        brick = pick_a_brick()
    return True

def game():
    global game_status
    cont = step()
    if cont == False:
        screens.create_screen("GAME OVER\nYOUR SCORE: "+str(score), "PLAY AGAIN", "QUIT")
        game_status = 3
        return
    if game_status == 1:
        canvas.after(500, game)

#-----------------------------------------------------------------------------------------
# Arrow keys binding functions:
#-----------------------------------------------------------------------------------------

def left_arrow(event):
    global brick
    global game_status
    if game_status == 1:
        go_left(brick[0])

def right_arrow(event):
    global brick
    global game_status
    if game_status == 1:
        go_right(brick[0])

def up_arrow(event):
    global brick
    global game_status
    if game_status == 1:
        choose_rotation(brick)
    
def down_arrow(event):
    global game_status
    if game_status == 1:
        step()


#-----------------------------------------------------------------------------------------
# Mouse click binding functions:
#-----------------------------------------------------------------------------------------

def left_click(event):
    global game_status
    if game_status == 1:
        x0 = screens.pause_button_coords[0]
        y0 = screens.pause_button_coords[1]
        x1 = screens.pause_button_coords[2]
        y1 = screens.pause_button_coords[3]
        if event.x > x0 and event.x < x1 and event.y > y0 and event.y < y1: # if the player clicked inside the pause button
            game_status = 2
            screens.create_screen("PAUSED", "RESUME", "QUIT")
    else:
        click_analysis(event.x, event.y)
    

def click_analysis(x, y):
    global game_status
    global score
    global brick
    if x > screens.buttons_x0 and x < screens.buttons_x1:
        if y > screens.button1_y0 and y < screens.button1_y1:
            screens.remove_screen()
            if game_status == 0:
                game_status = 1
                screens.walls()
                screens.bottom()
                screens.create_grid()
                screens.scoreboard()
                screens.pause_button()
                game()

            if game_status == 2:
                game_status = 1
                game()

            elif game_status == 3:
                game_status = 1
                screens.reset_grid()
                score = 0
                screens.score_print(score)
                brick = pick_a_brick()
                game()

        elif y > screens.button2_y0 and y < screens.button2_y1:
            root.destroy()
