from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.tires import Tires


class CarFactory:

    @staticmethod
    def makePalindrome(current_date, last_service_date, warning_light_is_on, tire_sensor):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = tire_sensor
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def createRorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = tire_sensor
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def makeThovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = tire_sensor
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def makeGlissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = tire_sensor
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def makeCalliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensor):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = tire_sensor
        car = Car(engine, battery, tire)
        return car