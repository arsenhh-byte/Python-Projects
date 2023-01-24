import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("aquamarine")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g , b)
    return color

directions = [0, 90, 180, 270]
tim.width(10)
tim.speed(20)
for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random_color())
    tim.width(10)

screen = Screen()
screen.exitonclick()