from turtle import Turtle, Screen
import time
from Day_20_Snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
#Snake body

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Snake movement
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


#Control Snake movement

#Collision with food

#Scoreboard

#Gameover = Collision with wall

#Gameover = Collision with itself
screen.exitonclick()