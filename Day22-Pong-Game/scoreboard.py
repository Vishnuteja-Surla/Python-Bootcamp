# Importing Modules
import turtle

# Constants


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 50, "normal"))

    def left_score(self):
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.r_score += 1
        self.update_score()