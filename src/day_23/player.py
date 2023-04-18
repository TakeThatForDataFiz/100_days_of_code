STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def fwd(self):
        self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)

    def check_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)
