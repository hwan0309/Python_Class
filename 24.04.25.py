import turtle as t
import random
tu = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tu.pensize(15)
tu.speed(10)

for _ in range(200):
    tu.color(random_color())
    tu.forward(30)
    tu.setheading(random.choice(directions))
