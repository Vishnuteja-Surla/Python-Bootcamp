import turtle
import random

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_WIDTH = 0.75
CAR_LENGTH = 1.5

class CarManager:
    
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = turtle.Turtle(shape="square")
        car.shapesize(stretch_wid=CAR_WIDTH, stretch_len=CAR_LENGTH)
        car.penup()
        car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        car.goto((320, random_y))
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        for c in self.cars:
            c.forward(self.move_distance)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT