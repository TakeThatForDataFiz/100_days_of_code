import turtle


def draw_dotted_line(turtle, n):
    turtle.pd()
    turtle.fd(n)
    turtle.pu()
    turtle.fd(n)


if __name__ == "__main__":
    t = turtle.Turtle()
    for _ in range(15):
        draw_dotted_line(t, 15)
    screen = turtle.Screen()
    screen.exitonclick()
