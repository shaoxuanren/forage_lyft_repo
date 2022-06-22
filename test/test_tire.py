import unittest

from tire.carrigan_tires import carriganTires
from tire.octoprime_tires import octoprimeTires
from tire.tires import Tires

class Test_carriganTires(unittest.TestCase):
    def tires_need_to_be_serviced(self):
        tire_wear = [0.9, 0.1, 0.4, 0.2]
        tires = carriganTires(tire_wear)
        self.assertTrue(tires.needs_service)

    def tires_need_not_to_be_serviced(self):
        tire_wear = [0.7, 0.1, 0.4, 0.2]
        tires = carriganTires(tire_wear)
        self.assertFalse(tires.needs_service)

class Test_carriganTires(unittest.TestCase):
    def tires_need_to_be_serviced(self):
        tire_wear = [1, 1, 1, 0.2]
        tires = carriganTires(tire_wear)
        self.assertTrue(tires.needs_service)

    def tires_need_not_to_be_serviced(self):
        tire_wear = [0.7, 0.1, 0.4, 0.2]
        tires = carriganTires(tire_wear)
        self.assertFalse(tires.needs_service)
