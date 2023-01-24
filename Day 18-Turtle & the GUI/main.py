from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("aquamarine")

# Drawing a square
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# Drawing dashed lines

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()
