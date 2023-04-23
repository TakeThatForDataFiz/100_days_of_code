import random
from car import Car
import time 

NUM_CARS = 10

class CarManager:
    def __init__(self):
        self.cars = []

    def spawn(self):
        for _ in range(NUM_CARS):
#            time.sleep(random.random())
            car = Car()
            self.cars.append(car)

    def move(self):
        for car in self.cars:
           car.move() 

    def reset(self):
        for car in self.cars:
            car.reset()
        self.cars = []
