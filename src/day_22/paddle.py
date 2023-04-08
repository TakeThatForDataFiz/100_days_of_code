from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.xpos = xpos
        self.ypos = ypos
        self.pu()
        self.goto(x=self.xpos, y=self.ypos)
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=1)

    def move_up(self):
        self.ypos = self.ycor() + 20
        self.goto(x=self.xcor(), y=self.ypos)

    def move_down(self):
        self.ypos = self.ycor() - 20
        self.goto(x=self.xcor(), y=self.ypos)
