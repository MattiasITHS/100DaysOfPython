from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.color("red")
# moving the turtle in a square
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)


screen.exitonclick()