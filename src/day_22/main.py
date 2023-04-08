from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

HEIGHT = 600
BGCOLOR = "black"
WIDTH = 800


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor(BGCOLOR)
    screen.title("Pong Python Game")
    screen.tracer(0)
    rpaddle = Paddle(xpos=350, ypos=0)
    lpaddle = Paddle(xpos=-350, ypos=0)
    scoreboard = ScoreBoard()
    ball = Ball(paddles=[lpaddle, rpaddle], scoreboard=scoreboard)
    L_KEYS = [(lpaddle.move_up, "w"), (lpaddle.move_down, "s")]
    R_KEYS = [(rpaddle.move_up, "Up"), (rpaddle.move_down, "Down")]
    for f, key in [*L_KEYS, *R_KEYS]:
        screen.onkeypress(fun=f, key=key)
    screen.listen()
    is_game_on = True
    while is_game_on:
        screen.update()
        ball.move()
    screen.exitonclick()
