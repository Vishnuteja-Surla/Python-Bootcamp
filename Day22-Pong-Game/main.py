# Importing Modules
import turtle
import time
import paddle
import ball
import scoreboard

# Constants
WIDTH = 800
HEIGHT = 600
RIGHT_PADDLE_POS = (350, 0)
LEFT_PADDLE_POS = (-350, 0)

# Main Code
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = paddle.Paddle(RIGHT_PADDLE_POS)
l_paddle = paddle.Paddle(LEFT_PADDLE_POS)

ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

game_on = True

while game_on:
    time.sleep(ball.time_skip)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if ball.distance(l_paddle) < 60 and ball.xcor() < LEFT_PADDLE_POS[0] + 20 or ball.distance(r_paddle) < 60 and ball.xcor() > RIGHT_PADDLE_POS[0] - 20:
        ball.speed_up()
        ball.bounce_paddle()
    if ball.xcor() < LEFT_PADDLE_POS[0]-30:
        ball.restart()
        scoreboard.right_score()
    if ball.xcor() > RIGHT_PADDLE_POS[0]+30:
        ball.restart()
        scoreboard.left_score()

screen.exitonclick()