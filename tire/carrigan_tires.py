from asyncio import FastChildWatcher
from turtle import Turtle
from tire.tires import Tires

class carriganTires(Tires):

    def __init__(self, tire_sensor) -> None:
        self.tire_sensor = tire_sensor
    
    def needs_service(self):
        for each_tire in self.tire_sensor:
            if each_tire >= 0.9:
                return True

            return False
        