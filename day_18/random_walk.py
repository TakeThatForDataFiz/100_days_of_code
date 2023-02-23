import random
import turtle


def get_random_hex_color():
    # remove first 2 digits of hex number and add # to make valid color code
    hex_num = hex((random.randint(0, 16777215)))[2:]
    return '#' + f"{hex_num:06s}"


def get_random_direction():
    return (random.randint(1, 4))*90


def set_turtle(turtle):
    turtle.speed(0)
    turtle.pensize(10)
    turtle.width(width=10)
    turtle.hideturtle()


def random_turtle_move(turtle):
    hex_color = get_random_hex_color()
    turtle.pencolor(hex_color)
    angle = get_random_direction()
    turtle.fd(15)
    turtle.setheading(angle)


if __name__ == '__main__':
    t = turtle.Turtle()
    set_turtle(t)
    for _ in range(1000):
        random_turtle_move(t)
    screen = turtle.Screen()
    screen.exitonclick()
