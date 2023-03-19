from turtle import Turtle, Screen
import turtle
import random

COLORS = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')


def move_fd_random(turtle):
    turtle.fd(random.randint(1, 10))

def create_turtle(color, pos):
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.color(color)
    turtle.pu()
    turtle.goto(x=-500, y=pos*30)
    return turtle

def check_width(input_turtle, guess):
    if input_turtle.xcor() >= (turtle.window_width() / 2) - 25:
        if guess.lower() == input_turtle.color()[0]:
            print("Congrats you guessed correctly")
        else:
            print("Sorry you guessed wrong.")
        print(f"The {input_turtle.color()[0].title()} Turtle won the race.")
        return False
    else:
        return True

def check_width_wrapper(guess):
    for input_turtle in turtle.turtles():
        flag = check_width(input_turtle=input_turtle, guess=guess)
        if flag is False:
            return False
        else:
            move_fd_random(turtle=input_turtle)
    return True
    



if __name__ == '__main__':
    screen = Screen()
    guess = turtle.textinput("Please enter Turtle Race Bet", "Color")
    for ypos, color in enumerate(COLORS, start=1):
        new_turtle = create_turtle(color=color, pos=ypos)
    check_width_flag = True
    while check_width_flag:
        check_width_flag = check_width_wrapper(guess=guess)
    screen.bye()


