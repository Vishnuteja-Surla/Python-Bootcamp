import turtle
import random

t = turtle.Turtle()
turtle.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


t.speed(0)

angle = 5

for i in range(360//angle):
    t.color(random_colour())
    t.circle(100)
    t.right(angle)

screen = turtle.Screen()
screen.exitonclick()