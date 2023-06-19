import turtle

# Constants
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-250, 280)
        self.hideturtle()
        self.speed("fastest")
        self.score = 0
        self.write(f"Level : {self.score}", False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level : {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)