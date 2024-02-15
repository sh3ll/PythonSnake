#Steg 2 - Riktig vindu størrelse

import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

#-------------
#+++++++++++++#
canvas.pack()
window.update()
#-------------

window.mainloop()