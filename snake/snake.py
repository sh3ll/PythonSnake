import random
import tkinter
import window
import tile

#Vars
velocityX = 0
velocityY = 0
rows = 25
cols = 25
game_over = False
score = 0

windowsize = window.Window

#Window Size
WINDOW_WIDTH = windowsize.size(rows, cols)
WINDOW_HEIGHT = windowsize.size(rows, cols)
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
snake = tile.Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
food = tile.Tile(10 * TILE_SIZE, 10 * TILE_SIZE)

snake_body = []

def change_direction(e):
    global velocityX, velocityY
    if(game_over):
        return

    #print(e.keysym)
    if(e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1 ):
        velocityX = 1
        velocityY = 0   

def move():
    global snake, food, snake_body, game_over, tile, score

    if(game_over):
        return
    
    if(snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return

    for tiles in snake_body:
        if(snake.x == tiles.x and snake.y == tiles.y):
            game_over = True
            return

    #collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(tile.Tile(food.x, food.y))
        food.x = random.randint(0, cols-1) * TILE_SIZE
        food.y = random.randint(0, rows-1) * TILE_SIZE
        score += 1

    #snake body
    for i in range (len(snake_body)-1, -1, -1):
        tiles = snake_body[i]
        if(i==0):
            tiles.x = snake.x
            tiles.y = snake.y
        else:
            prev_tile = snake_body [i-1]
            tiles.x = prev_tile.x
            tiles.y = prev_tile.y 

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw(): 
    global snake, food, snake_body, game_over, score 
    move()

    canvas.delete("all")

    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "hotpink")
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime")

    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "lime")

    if(game_over):
        canvas.create_text(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, font = "Arial 20", text = f"Game Over! Score: {score}", fill = "white")
    else:
        canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {score}", fill = "white")

    window.after(100, draw)

draw()

#Window Looping
window.bind("<KeyRelease>", change_direction)
window.mainloop()
