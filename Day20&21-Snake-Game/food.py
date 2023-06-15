#Importing Modules
import turtle
import random


# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


#Creating the Food class by inherting from the Turtle class
class Food(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.reposition()

    def reposition(self):
        self.goto(random.randint(-(SCREEN_WIDTH/2 - 30), (SCREEN_WIDTH/2 - 30)), random.randint(-(SCREEN_HEIGHT/2 - 30), (SCREEN_HEIGHT/2 - 30)))
