from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_COR = 100
Y_START, Y_STOP = (40, 280)
CAR_DIST = 30

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.shapesize(stretch_wid=0.7, stretch_len=1.4, outline=1)
        color = random.choice(seq=COLORS)
        self.color(color)
        self.goto(x=X_COR, y=random.randrange(start=Y_START, stop=Y_STOP, step=CAR_DIST))

    def move(self):
        self.goto(x=self.xcor() - MOVE_INCREMENT, y=self.ycor())



               
