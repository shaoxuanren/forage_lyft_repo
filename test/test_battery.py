import unittest
from datetime import date, timedelta
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class Testnubbin_battery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.fromisoformat("2022-06-21")
        last_service_date = date.fromisoformat("2015-03-21")
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = date.fromisoformat("2022-06-21")
        last_service_date = date.fromisoformat("2022-01-01")
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

class Testsspindler_battery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = date.fromisoformat("2022-06-21")
        last_service_date = date.fromisoformat("2020-03-16")
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())    

    def test_battery_should_not_be_serviced(self):
        today = date.fromisoformat("2022-06-21")
        last_service_date = date.fromisoformat("2021-03-18")
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())



