# from turtle import Turtle, Screen, Shape
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
#
#
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Charmander","Squirtle","Bulbasaur","Pikachu"])
table.add_column("Type",["Fire","Water","Grass","Electric"])
table.align = "l"
print(table)
