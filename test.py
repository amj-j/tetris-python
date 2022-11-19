import tkinter
root = tkinter.Tk()

canvas_height = 600
canvas_width = 800
canvas = tkinter.Canvas(root, height = canvas_height, width = canvas_width, background = "#D7D7D7")
canvas.pack()

screen_x1 = int(canvas_width/4)
screen_y1 = int(canvas_height/4)
screen_x2 = screen_x1*3
screen_y2 = screen_y1*3

buttons_x1 = int(canvas_width/8)*3
button1_y1 = int(canvas_width/24)*7
button2_y1 = int(canvas_width/24)*10
buttons_x2 = int(canvas_width/8)*5
button1_y2 = int(canvas_width/24)*9
button2_y2 = int(canvas_width/24)*12

def screen():
    #canvas.create_rectangle([screen_x1, screen_y1, screen_x2, screen_y2], width = 10,  fill = "#D7D7D7")
    button1 = canvas.create_rectangle(buttons_x1, button1_y1, buttons_x2, button1_y2, width = 5,  fill = "#D7D7D7")
    button2 = canvas.create_rectangle(buttons_x1, button2_y1, buttons_x2, button2_y2, width = 5,  fill = "#D7D7D7")

def down_arrow(event):
    root.destroy()

screen()

root.bind('<Down>', down_arrow)

root.mainloop()