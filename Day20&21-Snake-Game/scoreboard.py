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
        with open("highscore.txt") as hs:
            self.highscore = int(hs.read())
        self.write(f"Score : {self.score} High Score : {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def game_reset(self):
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as hs:
                hs.write(str(self.score))
            with open("highscore.txt") as hs:
                self.highscore = int(hs.read())
        self.score = 0
        self.update_screen()