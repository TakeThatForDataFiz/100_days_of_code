from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20


class Snake:
    def __init__(self):
        self.segments = []
        for xpos, ypos in STARTING_POSITIONS:
            new_t = self.create_snake(xpos=xpos, ypos=ypos)
            self.segments.append(new_t)
        self.head = self.segments[0]

    def create_snake(self, xpos, ypos):
        t = Turtle()
        t.pu()
        t.goto(xpos, ypos)
        t.pencolor("white")
        t.fillcolor("white")
        t.shape("square")
        return t

    def _move_sq(self, turtle, pos):
        x, y = pos
        turtle.goto(x, y)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def move(self):
        reverse_sq = list(reversed(self.segments))
        for idx, sq in enumerate(reverse_sq):
            try:
                self._move_sq(
                    turtle=sq,
                    pos=(reverse_sq[idx + 1].xcor(), reverse_sq[idx + 1].ycor()),
                )
            # head of the snake will cause indexerror
            except IndexError:
                self._move_sq(
                    turtle=sq,
                    pos=(reverse_sq[idx].xcor() + MOVE_DIST, reverse_sq[idx].ycor()),
                )
