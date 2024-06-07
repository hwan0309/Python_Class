import turtle as t
import random

tu = t

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tu.speed(10)

def draw_wpirograph(size_of_gap):
    for _ in range(360/size_of_gap):
        tu.circle(100)
        tu.color(random_color())

        tu.setheading(tu.heading()+size_of_gap)

draw_wpirograph(5)

screen = t.Screen()
screen.exitonclick()
