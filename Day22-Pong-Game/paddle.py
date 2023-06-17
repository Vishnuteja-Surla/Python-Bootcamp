# Importing Modules
import turtle

# Constants
STRETCH_WIDTH = 0.5
STRETCH_LEN = 5
MOVEMENT = 25


class Paddle(turtle.Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LEN)
        self.penup()
        self.goto(x = pos[0], y = pos[1])
        self.setheading(90)
        self.color("white")

    def up(self):
        self.forward(MOVEMENT)
    
    def down(self):
        self.back(MOVEMENT)