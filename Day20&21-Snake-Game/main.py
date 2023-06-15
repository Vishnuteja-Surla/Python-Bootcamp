#Importing Modules
import turtle
import time
import snake
import food
import scoreboard


# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# Initial Setup
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

# Listening to key strokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

# Animating the Snake to move by itself

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.reposition()
        snake.extend()
        scoreboard.increment_score()

    #Detect collision with wall
    if snake.head.xcor() > (SCREEN_WIDTH/2 - 20) or snake.head.xcor() < -(SCREEN_WIDTH/2 - 20) or snake.head.ycor() > (SCREEN_HEIGHT/2 - 20) or snake.head.ycor() < -(SCREEN_WIDTH/2 - 20):
        game_on = False
        scoreboard.game_over()
    
    #Detect collision with tail
    for i in snake.snake:
        if snake.head != i and snake.head.distance(i) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()