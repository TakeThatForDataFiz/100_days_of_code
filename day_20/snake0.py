from turtle import Turtle, Screen

def create_square(xpos, ypos):
    t = Turtle()
    t.pu()
    t.goto(xpos, ypos)
    t.pencolor("white")
    t.fillcolor("white")
    t.shape("square")
    return t

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    starting_xpos = (0, -20, -40)
    for idx in range(3):
        create_square(xpos=starting_xpos[idx], ypos=0)
    screen.exitonclick()