import turtle

# dimensions
WIDTH = 500
HEIGHT = 500
DELAY = 400

# move snake
def move():
    # remove existing stamps
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += 20

    snake.append(new_head)
    snake.pop(0)

    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()

    screen.update()

    turtle.ontimer(move, DELAY)


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

# set animation
move()

# finish game
turtle.done()