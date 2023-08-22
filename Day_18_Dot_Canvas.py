# import colorgram
import turtle
import turtle as turtle_module
import random
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, b , g)
#     rgb_colors.append(new_color)
# print(rgb_colors)
pen = turtle_module.Turtle()
turtle.colormode(255)
pen.speed("fastest")
pen.penup()
pen.hideturtle()
color_list = [(199, 117, 175), (124, 24, 36), (210, 213, 221), (168, 57, 106), (222, 227, 224), (186, 53, 158), (6, 83, 57), (109, 85, 67), (113, 175, 161), (22, 174, 122), (64, 138, 153), (39, 36, 36), (76, 48, 40), (9, 47, 67), (90, 53, 141), (181, 79, 96), (132, 42, 40), (210, 151, 200), (141, 155, 171), (179, 186, 201), (172, 159, 153), (212, 177, 183), (176, 203, 198), (150, 120, 115), (202, 190, 185), (40, 82, 72), (46, 62, 73), (47, 82, 66)]

pen.setheading(220)
pen.forward(320)
pen.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    pen.dot(20, random.choice(color_list))
    pen.forward(50)
    if dot_count % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()