import random
import tkinter
import window
import tile

windowsize = window.Window

#Window Size
WINDOW_WIDTH = windowsize.size(25, 25)
WINDOW_HEIGHT = windowsize.size(25, 25)
TILE_SIZE = 25

#Game Window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

#Window Canvas
canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
canvas.pack()
window.update()

#Window Center
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = windowsize.windowcenter(screen_width, window_width)
window_y = windowsize.windowcenter(screen_height, window_height)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#Game Init
snake = tile.Tile(TILE_SIZE, 5)
food = tile.Tile(TILE_SIZE, 10)

def draw():
    global snake

    canvas.create_rectangle(snake.x, snake.y, snake.tile_x, snake.tile_y, fill = "lime")
    canvas.create_rectangle(food.x, food.y, food.tile_x, food.tile_y, fill = "hotpink")

    window.after(100, draw)

draw()

#Window Looping
window.mainloop()

#print ("WIDTH: " + str(WINDOW_WIDTH) + " HEIGHT: " + str(WINDOW_HEIGHT))