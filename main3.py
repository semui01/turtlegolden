# Turtle running

from turtle import Turtle, Screen
import random

is_race_on = False

# create turtle class ,screen, and size of the screen
screen = Screen()
width = 700
height = 600
number_of_turtles =6
screen.setup(width=width, height=height)
user_bet = screen.textinput(title='Make your Bet', prompt='which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

x_position = -width / 2 + 30
y_positions = -height / 2 + 50
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x_position, y=y_positions + turtle_index * int((height-50)/number_of_turtles))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > (width / 2 - 20):
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You ve won! the {winning_color} turtle is the winner!')

            else:
                print(f'You ve lost! you picked {user_bet} turtle,but the {winning_color} turtle is the winner!')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
