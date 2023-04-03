from turtle import Screen, Turtle

t = Turtle()
screen = Screen()


def move_bk():
    t.bk(10)


def move_fwd():
    t.fd(10)


def turn_left():
    t.left(45)


def turn_right():
    t.right(45)


def reset_screen():
    t.reset()


if __name__ == "__main__":
    screen.listen()
    func_dict = {
        move_fwd: "w",
        turn_left: "a",
        move_bk: "s",
        turn_right: "d",
        reset_screen: "c",
    }

    for func, key in func_dict.items():
        screen.onkey(key=key, fun=func)

    screen.exitonclick()
