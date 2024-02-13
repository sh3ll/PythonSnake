#Steg 4 - Snake

import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

#-------------
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#-------------

window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

#Window Center
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
#Geometry Format - (width)*(height)+(x)+(y)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#-------------
#Game Init
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)

def draw():
    global snake

    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime green")
    window.after(100, draw)

draw()
#-------------

window.mainloop()