# Converting tkinter library functions to simpler functions suited for this program

import tkinter
from tkinter.font import Font
root = tkinter.Tk()

east = tkinter.E
west = tkinter.W
center = tkinter.CENTER
text_font = Font(family = "Helvetica", size = 22, weight = "bold")

canvas_height = 600
canvas_width = 800
blocksize = 30 # size of a block

canvas = tkinter.Canvas(root, height = canvas_height, width = canvas_width, background = "#FFFFC5")

def initial_settings():
    root.title("Tetris")
    #root.geometry('200x200')
    #root.config(bg='#345')


#-----------------------------------------------------------------------------------------
# Tetris itself consists only of square blocks.
# Here are tkinter library functions simplified for creating blocks:
#-----------------------------------------------------------------------------------------

def create_block(x,y, color): #creates a block of blocksize
    x1 = x*blocksize
    y1 = y*blocksize
    x2 = (x+1)*blocksize
    y2 = (y+1)*blocksize
    return canvas.create_rectangle(x1, y1, x2, y2, width = 2,  fill = color)

def block_pos(block): #returns position of given block (coordinations in blocksize unit)
    x = int(canvas.coords(block)[0]/blocksize)
    y = int(canvas.coords(block)[1]/blocksize)
    return x,y

def down(block): #moves given block one tile down
    canvas.move(block, 0, blocksize)

def right(block):
    canvas.move(block, blocksize, 0)

def left(block):
    canvas.move(block, -blocksize, 0)

def movexy(block, x, y):
    canvas.move(block, x*blocksize, y*blocksize)

def remove(block):
    canvas.delete(block)

