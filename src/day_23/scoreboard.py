FONT = ("Courier", 18, "bold")
POS = (-300, 270)
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.pu()
        self.goto(POS)
        self.score = 0
        self.update_brd(incr=1)

    def update_brd(self, incr):
        self.clear()
        self.score += incr
        self.write(f"Level {self.score}", align="left", font=FONT)

