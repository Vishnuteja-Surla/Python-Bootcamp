import turtle

def forward():
    t.forward(20)

def back():
    t.back(20)

def left():
    t.left(10)

def right():
    t.right(10)

def reset():
    t.home()
    t.clear()


t = turtle.Turtle()
screen = turtle.Screen()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(back, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(reset, "c")

screen.exitonclick()