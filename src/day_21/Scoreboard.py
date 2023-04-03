from turtle import Turtle

XPOS = -30
YPOS = 280
INCR = 1
ALIGN = "center"
FONT = ("Consolas", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(XPOS, YPOS)
        self._display()

    def add(self):
        self.score += INCR
        self._display()

    def _display(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align=ALIGN, font=FONT)
