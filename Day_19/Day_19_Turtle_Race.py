from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color? 'yellow', "
                                                          "'blue', 'red', 'green', 'purple', 'orange'")
y_pos = 100 # each turtle position y-axis
colors = ["yellow", "blue", "red", "green", "purple", "orange"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos)
    y_pos = y_pos - 25
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winner is {winning_color}")
            else:
                print(f"You loose! The winner was {winning_color}")
            is_race_on = False
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
