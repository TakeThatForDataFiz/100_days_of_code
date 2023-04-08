from turtle import Turtle
import time


SLEEP = 0.005
XCOR_PADDLE = 320
BOUND = 380


class Ball(Turtle):
    def __init__(self, paddles, scoreboard):
        super().__init__()
        self.pu()
        self.x_dist = 1.0
        self.y_dist = 1.5
        self.paddles = paddles
        self.scoreboard = scoreboard
        self.shape("circle")
        self.color("white")

    def _bounce(self, is_ver, is_hor):
        if is_ver:
            self.y_dist *= -1
        if is_hor:
            self.x_dist *= -1

    def _reset(self):
        self.x_dist *= -1
        self.goto(x=0, y=0)

    def move(self):
        # check for wall collisions
        if self.ycor() > 290 or self.ycor() < -285:
            self._bounce(is_ver=True, is_hor=False)
        # check for paddle collisions
        for paddle in self.paddles:
            if self.distance(paddle) < 50 and (
                self.xcor() > XCOR_PADDLE or self.xcor() < -XCOR_PADDLE
            ):
                self._bounce(is_ver=True, is_hor=True)
        # check for boundary
        if self.xcor() > BOUND or self.xcor() < -BOUND:
            is_left = self.xcor() < -XCOR_PADDLE
            self.scoreboard.score(is_lscore=is_left)
            self._reset()
        new_x = self.xcor() + self.x_dist
        new_y = self.ycor() + self.y_dist
        # use sleep to slow computer down to human readable speed
        time.sleep(SLEEP)
        # .77 = scale to ensure ball travels at correct slope
        self.goto(x=new_x, y=new_y)
