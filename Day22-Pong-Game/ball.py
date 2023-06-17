# Importing Modules
import turtle

# Constants
STRETCH_WIDTH = 0.5
STRETCH_LEN = 0.5


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LEN)
        self.penup()
        self.color("white")
        self.xmov = 10
        self.ymov = 10
        self.time_skip = 0.1

    def move(self):
        x = self.xcor() + self.xmov
        y = self.ycor() + self.ymov
        self.goto(x,y)

    def bounce_wall(self):
        self.ymov *= -1

    def bounce_paddle(self):
        self.xmov *= -1

    def restart(self):
        self.goto(0,0)
        self.xmov *= -1
        self.time_skip = 0.1

    def speed_up(self):
        self.time_skip *= 0.9