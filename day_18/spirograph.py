import turtle
import random
from random_walk import get_random_hex_color


def make_tilt_circle(turtle, radius, tilt):
    hex_color = get_random_hex_color()
    turtle.pencolor(hex_color)
    turtle.circle(radius=radius)
    turtle.setheading(tilt)


if __name__ == '__main__':
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.width(4)
    tilt = 5
    for angle in range(360)[1::tilt]:
        make_tilt_circle(turtle=t, radius=250, tilt=angle)
    screen = turtle.Screen()
    screen.exitonclick()
