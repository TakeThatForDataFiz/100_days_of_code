from turtle import Turtle, Screen
t = Turtle()
screen = Screen()

def move_t_fwd():
    move_fwd(turtle=t, num=10)

def move_fwd(turtle, num):
    turtle.forward(num)

# need to pair with event listener
if __name__ == '__main__':
    screen.listen()
    screen.onkey(key="space", fun=move_t_fwd)
    screen.exitonclick()