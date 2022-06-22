from tire.tires import Tires

class octoprimeTires(Tires):

    def __init__(self, tire_sensor):
        self.tire_sensor = tire_sensor

    def needs_service():
        return sum(sum.tire_sensor) >= 3.0
