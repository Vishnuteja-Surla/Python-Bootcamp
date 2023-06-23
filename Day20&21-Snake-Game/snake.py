#Importing Modules

import turtle

# Constants
MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        # Creating the Snake's Initial Body
        for i in range(3):
            t = turtle.Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(i * -20, 0)
            self.snake.append(t)

    def extend(self):
        t = turtle.Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(self.snake[-1].position())
        self.snake.append(t)

    # Recreating the snake and repositioning the previous snake out of screen
    def snake_reset(self):
        for i in self.snake:
            i.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        # Moving a segment of the snake to the position of it's previous segment
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].xcor(), self.snake[i-1].ycor())
        self.head.forward(MOVEMENT_DISTANCE)

    # Changing the direction of the snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)