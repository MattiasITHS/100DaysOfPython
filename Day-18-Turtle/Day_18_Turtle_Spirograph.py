import turtle
from turtle import *
import random


# Set up the turtle
screen = Screen()
screen.bgcolor("white")
screen.title("Spirograph")

pen = Turtle()
pen.speed("fastest")  # Set drawing speed to maximum
turtle.colormode(255)


def random_colors():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_colors = (r, b, g)
    return random_colors


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pen.color(random_colors())
        pen.circle(100)
        pen.setheading(pen.heading() + size_of_gap)


draw_spirograph(5)

screen.exitonclick()
