import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
brd = Scoreboard()
car_mgr = CarManager()
screen.onkeypress(player.fwd, "Up")
screen.listen()
game_is_on = True
car_mgr.spawn()
while game_is_on:
    time.sleep(0.1)
    car_mgr.move()
    if player.check_finish():
        brd.update_brd(incr=1)
        player.reset()
    screen.update()

