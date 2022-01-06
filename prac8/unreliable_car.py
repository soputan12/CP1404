from car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance): #generate between 0-100
        random_num = random.randint(1, 100)
        if random_num >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
