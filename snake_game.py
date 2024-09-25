import tkinter as tk
import random

r = 20
c = 20
tile_size = 20

window_width = tile_size * r
window_height = tile_size * c

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

window = tk.Tk()
window.title("SNAKE GAME")

canvas = tk.Canvas(window, bg="black", width=window_width, height=window_height)
canvas.pack()

window.update()

window_height = window.winfo_height()
window_width = window.winfo_width()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

snake = Tile(5 * tile_size, 5 * tile_size)
food = Tile(10 * tile_size, 10 * tile_size)
snake_body = []
velocity_x = 0
velocity_y = 0
over = False

def change_direction(e):
    global velocity_x, velocity_y, over
    if over:
        return

    if e.keysym == "Up" and velocity_y != 1:
        velocity_x = 0
        velocity_y = -1
    elif e.keysym == "Down" and velocity_y != -1:
        velocity_x = 0
        velocity_y = 1
    elif e.keysym == "Left" and velocity_x != 1:
        velocity_x = -1
        velocity_y = 0
    elif e.keysym == "Right" and velocity_x != -1:
        velocity_x = 1
        velocity_y = 0

def move():
    global snake, food, snake_body, over
    if over:
        return

    if snake.x < 0 or snake.x >= window_width or snake.y < 0 or snake.y >= window_height:
        over = True
        return

    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            over = True
            return

    if snake.x == food.x and snake.y == food.y:
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, r - 1) * tile_size
        food.y = random.randint(0, c - 1) * tile_size

    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i].x = snake_body[i - 1].x
        snake_body[i].y = snake_body[i - 1].y

    if snake_body:
        snake_body[0].x = snake.x
        snake_body[0].y = snake.y

    snake.x += velocity_x * tile_size
    snake.y += velocity_y * tile_size
    
def draw():
    move()
     
    canvas.delete("all")
    
    canvas.create_rectangle (snake.x, snake.y, snake.x + tile_size, snake.y + tile_size, fill = "blue")
    canvas.create_rectangle (food.x, food.y, food.x + tile_size, food.y + tile_size, fill = "lime green")
    for tile  in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + tile_size, tile.y + tile_size, fill = "blue")
   
    window.after(100, draw)
    

window.bind("<KeyPress>", change_direction)
draw ()
window.mainloop()