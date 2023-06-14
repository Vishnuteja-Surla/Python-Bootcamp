import turtle

t = turtle.Turtle()

for c in range(10):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)

screen = turtle.Screen()
screen.exitonclick()