#Importing Modules
import turtle


# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, SCREEN_HEIGHT/2 - 20)
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)