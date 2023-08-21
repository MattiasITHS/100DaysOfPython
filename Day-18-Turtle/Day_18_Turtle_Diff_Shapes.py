from turtle import Turtle, Screen
import random

import colours as colours

tim = Turtle()
screen = Screen()
tim.shape("turtle")

# for square in range(4):
#     tim.pencolor("red")
#     tim.forward(90)
#     tim.right(90)
#
# for triangle in range(3):
#     tim.forward(90)
#     tim.right(120)
#
# for pentagon in range(5):
#     tim.pencolor("green")
#     tim.forward(90)
#     tim.right(72)
#
# for hexagon in range(6):
#     tim.pencolor("blue")
#     tim.forward(90)
#     tim.right(60)
#
# for heptagon in range(7):
#     tim.pencolor("purple")
#     tim.forward(90)
#     tim.right(51)
#
# for octagon in range(8):
#     tim.pencolor("pink")
#     tim.forward(90)
#     tim.right(45)
#
# for nonagon in range(9):
#     tim.pencolor("black")
#     tim.forward(90)
#     tim.right(40)
#
# for decagon in range(10):
#     tim.pencolor("yellow")
#     tim.forward(90)
#     tim.right(36)
colours = ["Blue", "SeaGreen", "Black", "Red", "Yellow", "SlateGrey"]

def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
