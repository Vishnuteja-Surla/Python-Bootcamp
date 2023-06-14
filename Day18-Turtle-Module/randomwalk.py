import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

t.pensize(10)
t.speed(0)
angle = [0, 90, 180, 270]

for i in range(100):
    t.color(random_colour())
    t.setheading(random.choice(angle))
    t.forward(20)

screen = turtle.Screen()
screen.exitonclick()