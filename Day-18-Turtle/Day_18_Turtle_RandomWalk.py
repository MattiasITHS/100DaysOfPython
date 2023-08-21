import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colours = ["Blue", "SeaGreen", "Black", "Red", "Yellow", "SlateGrey"]
direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(50)
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, b, g)
    return random_color

for _ in range(200):
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(direction))

screen.exitonclick()
