import colorgram
import turtle
import random


def get_colors_from_img(img, num_colors):
    colors = colorgram.extract(img, num_colors)
    # use guard to remove white shades
    return [
        color.rgb
        for color in colors
        if color.rgb.r < 240 or color.rgb.g < 240 or color.rgb.b < 240
    ]


def make_colored_circle(turtle, color):
    turtle.pd()
    turtle.dot(20, (color.r, color.g, color.b))


def move_pointer(turtle, dist):
    turtle.pu()
    turtle.fd(dist)


def set_paint_row(turtle, x, y):
    turtle.pu()
    turtle.setpos(x, y)


def run_turtle_painting(
    img,
    speed=0,
    num_colors=50,
    num_dots=630,
    x=-815,
    y=-500,
    row_size=30,
    dot_space=60,
    vert_space=50,
):
    t = turtle.Turtle()
    t.ht()
    t.speed(speed)
    screen = turtle.Screen()
    screen.colormode(255)
    set_paint_row(t, x, y)
    colors = get_colors_from_img(img, 50)
    for idx in range(num_dots):
        make_colored_circle(t, random.choice(colors))
        move_pointer(t, dot_space)
        if (idx + 1) % row_size == 0:
            y += vert_space
            set_paint_row(t, x, y)
    screen.exitonclick()


if __name__ == "__main__":
    run_turtle_painting("day_18\\hirst_painting\\sample_file.jpg")
