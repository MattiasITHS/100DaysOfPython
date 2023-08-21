from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()
tim.color("red")
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen.exitonclick()