import turtle

t = turtle.Turtle()
t.shape("turtle")

for c in range(4):
    t.forward(75)
    t.left(90)

screen = turtle.Screen()
screen.exitonclick()