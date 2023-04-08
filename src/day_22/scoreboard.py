from turtle import Turtle

FONT = ("Courier", 80, "normal")
SCORE_COORDS = [(-100, 200), (100, 200)]


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.rscore = 0
        self.lscore = 0
        self.goto(-100, 200)
        self._write_score()

    def _write_score(self):
        self.clear()
        for score, (xcor, ycor) in zip([self.lscore, self.rscore], SCORE_COORDS):
            self.goto(x=xcor, y=ycor)
            self.write(score, align="center", font=FONT)

    def score(self, is_lscore):
        if is_lscore:
            self.lscore += 1
        else:
            self.rscore += 1
        self._write_score()
