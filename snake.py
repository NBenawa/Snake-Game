import turtle
import random

# dimensions
WIDTH = 800
HEIGHT = 600
DELAY = 200
FOOD_SIZE = 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# movements
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

# move snake
def move():
    # remove existing stamps
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # check for collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else:
        snake.append(new_head)

        # checking food collision
        if not food_collision(): 
            snake.pop(0)

        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        screen.title(f'Snake Game.  Score: {score}')
        screen.update()

        turtle.ontimer(move, DELAY)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y1-y2) ** 2 + (x1-x2) ** 2) ** 0.5

def get_random_food_position():
    x = random.randrange(-WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randrange(-HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return (x, y)

def food_collision():
    global food_position, score
    if get_distance(snake[-1], food_position) < 20:
        score += 1
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def reset():
    global score, snake, snake_direction, food_position
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move()


# screen 
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("cyan")
screen.tracer(0)

# key controlling
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")

# stamper
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("red")
stamper.penup()

# snake
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
snake_direction = "up"
score = 0

# draw snake
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# food
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOOD_SIZE/20)
food.penup()
food_position = get_random_food_position()
food.goto(food_position)

# set animation
reset()

# finish game
turtle.done()