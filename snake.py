import turtle

# dimensions
WIDTH = 500
HEIGHT = 500
DELAY = 400

# screen 
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("cyan")

# stamper
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("red")
stamper.penup()

# snake
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# draw snake
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# finish game
turtle.done()