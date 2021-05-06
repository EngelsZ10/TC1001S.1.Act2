"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = ["black", "orange", "blue", "yellow", "green"]
color_food = randrange(5)
color_snake = randrange(5)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    if food.x<-200 or food.x>190 or food.y<-200 or food.y>190:
        food.x = 0
        food.y = 0
    food.x = food.x + randrange(-1,2)*10
    food.y = food.y + randrange(-1,2)*10

    if not inside(head) or head in snake:
        square(head.x, head.y, 15, 'red')
        update()
        return

    snake.append(head)

    if head==food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, color[color_snake])

    square(food.x, food.y, 9, color[color_food])
    update()
    ontimer(move, 100)

while color_snake == color_food:
    color_food = randrange(5)
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
