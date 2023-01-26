from turtle import Turtle
import random

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid= .5)
        self.color("violet")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)