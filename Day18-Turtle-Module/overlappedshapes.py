import turtle
import random

t = turtle.Turtle()

colours = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown']

for i in range(3,11):
    t.color(random.choice(colours))
    for j in range(i):
        t.right(360/i)
        t.forward(100)

screen = turtle.Screen()
screen.exitonclick()