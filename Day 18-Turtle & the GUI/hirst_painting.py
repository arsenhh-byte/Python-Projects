import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("aquamarine")
tim.penup()
tim.hideturtle()
turtle.colormode(255)
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 50)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


color_list = [(188, 19, 46), (244, 233, 64),  (195, 76, 34), (218, 66, 106), (13, 143, 89), (18, 125, 173), (196, 176, 17), (108, 182, 209), (12, 167, 214), (208, 154, 91), (238, 232, 3), (25, 40, 75), (36, 43, 111), (78, 175, 96), (181, 44, 65), (217, 67, 47), (217, 129, 153), (125, 185, 120), (238, 161, 180), (7, 61, 38), (147, 209, 220), (8, 91, 52), (5, 86, 109), (160, 30, 27), (237, 170, 163), (158, 211, 188), (87, 26, 62), (116, 119, 153), (181, 184, 213), (96, 26, 20)]

tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()