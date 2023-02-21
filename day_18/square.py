import turtle


def turn_turtle(turtle):
    turtle.fd(100)
    turtle.right(90)


if __name__ == '__main__':
    t = turtle.Turtle()
    for _ in range(4):
        turn_turtle(t)
    screen = turtle.Screen()
    screen.exitonclick()
