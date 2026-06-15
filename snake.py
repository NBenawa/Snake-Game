import turtle

# dimensions
WIDTH = 500
HEIGHT = 500

# screen 
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("cyan")

# snake
snake = turtle.Turtle()
snake.shape("circle")
snake.color("red")

# finish game
turtle.done()