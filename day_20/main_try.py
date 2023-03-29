from Snake import Snake
from turtle import Screen, Turtle
import time
    
def screen_setup():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)
    return screen

def create_listeners(screen, snake):
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')
    

if __name__ == "__main__":
    screen = screen_setup()
    snake = Snake()
    game_is_on = True
    while game_is_on:
        screen.update()
        create_listeners(screen=screen, snake=snake)
        time.sleep(0.1)
        snake.move()

    screen.exitonclick()
