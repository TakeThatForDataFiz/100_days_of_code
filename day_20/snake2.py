from turtle import Turtle, Screen
import time

def create_square(xpos, ypos):
    t = Turtle()
    t.pu()
    t.goto(xpos, ypos)
    t.pencolor("white")
    t.fillcolor("white")
    t.shape("square")
    return t


def move_sq(turtle, pos):
    x, y = pos
    turtle.goto(x, y)


def screen_setup():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    return screen


if __name__ == "__main__":
    screen = screen_setup()
    starting_xpos = (0, -20, -40)
    squares = []
    for idx in range(3):
        squares.append(create_square(xpos=starting_xpos[idx], ypos=0))
    screen.update()
    game_is_on = True
    reverse_sq = list(reversed(squares))
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        for idx, sq in enumerate(reverse_sq):
            try:
                move_sq(turtle=sq, pos=(reverse_sq[idx+1].xcor(), reverse_sq[idx+1].ycor()))
            # head of the snake will cause indexerror
            except IndexError:
                move_sq(turtle=sq, pos=(reverse_sq[idx].xcor() + 20, reverse_sq[idx].ycor()))

    screen.exitonclick()
