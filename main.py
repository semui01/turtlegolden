from turtle import *
import random

# prompt for input
n = input(f'How many sides would you like to draw?:')
m = input(f'How detail would you prefer(how many dots)?(e.g. :100):')
o = input(f'The size of the drawing dot?(e.g.: 1,2..):')

# resize the screen
screen = Screen()
screen.setup(1500,1500)

# create turtle object
bob = Turtle()

bob.setheading(200)


colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


bob.speed('fastest')
bob, hideturtle()

angle_draw = int(360 / int(n))
print(angle_draw)
pos_list = []

for _ in range(int(n)):
    # timmy_the_turtle.color('black')
    # timmy_the_turtle.hideturtle()
    bob.penup()
    bob.forward(200)
    pos_list.append(bob.pos())
    bob.dot(int(o), 'black')
    bob.right(angle_draw)

for _ in range(int(m)):
    # timmy_the_turtle.hideturtle()
    bob.penup()
    m_pos = random.choice(pos_list)
    distance = bob.distance(m_pos)
    bob.seth(bob.towards(m_pos))
    bob.forward(distance * 2 / 3)
    bob.dot(int(o), random_color())



screen = Screen()
screen.exitonclick()
