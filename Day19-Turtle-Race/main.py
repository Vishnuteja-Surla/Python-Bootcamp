import turtle
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)

race_on = False

user_bet = screen.textinput(title="Make a bet!",prompt="Which colour do you think will win? Enter a colour (Pick one from VIBGYOR): ")
print(user_bet)

colours = ['violet','silver','blue','green','yellow','orange','red']

turtles = []

for i in range(7):
    turtles.append(turtle.Turtle(shape="turtle"))

for i in range(7):
    turtles[i].color(colours[i])
    turtles[i].penup()
    turtles[i].goto(x=-280,y=-200+70*i)

if user_bet:
    race_on = True

while race_on:
    for i in turtles:
        dist = random.randint(0,20)
        i.forward(dist)
        if i.xcor() > 280:
            race_on = False
            if i.pencolor() == user_bet:
                print(f"You win! The {i.pencolor()} turtle won!")
            else:
                print(f"You lost! The {i.pencolor()} turtle won!")

screen.exitonclick()