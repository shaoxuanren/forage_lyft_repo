from battery.battery import Battery
from utilities import add_years


class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date


def needs_service(self):
        expired_date = add_years(self.last_service_date, 2)
        if expired_date < self.current_date:
            return True
        else:
            return False