from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colours = ["Blue", "SeaGreen", "Black", "Red", "Yellow", "SlateGrey"]
direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(50)

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(20)
    tim.setheading(random.choice(direction))

screen.exitonclick()
