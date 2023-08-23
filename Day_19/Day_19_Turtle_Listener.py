import turtle
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
pen.shape("turtle")


def move_forward():
    pen.forward(10)


def move_backward():
    pen.backward(10)


def turn_right():
    pen.right(10)


def turn_left():
    pen.left(10)


def reset_pen():
    pen.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset_pen)


screen.exitonclick()
