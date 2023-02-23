import turtle
import random


def get_random_hex_color():
    # remove first 2 digits of hex number and add # to make valid color code
    return '#' + hex(random.randint(0, 16777215))[2:]


def turn_turtle(turtle, angle):
    turtle.fd(100)
    turtle.right(angle)


def draw_shape(num_sides, turtle):
    hex_color = get_random_hex_color()
    turtle.pencolor(hex_color)
    for _ in range(num_sides):
        turn_turtle(turtle=turtle, angle=360/n)


if __name__ == '__main__':
    t = turtle.Turtle()
    # make up to ten sided shapes
    for n in range(11)[3:]:
        draw_shape(n, turtle)
    screen = turtle.Screen()
    screen.exitonclick()
