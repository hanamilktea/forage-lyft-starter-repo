from datetime import datetime
from CarFactory import CarFactory
from car import Car


class Battery:
    """
    Constructor representing Battery service criteria of the Car object. 
    Depending on type of battery, determines if the car needs to be serviced. 
    """
    def __init__(self, last_service_date, current_date):
        self._last_service_date = last_service_date
        self._current_date = current_date
        self.spindler = SpindlerBattery(self._last_service_date, self._current_date)
        self.nubbin = NubbinBattery(self._last_service_date, self._current_date)

    def battery_needs_service(self):
        return self.spindler.spindler_needs_service() or self.nubbin.nubbin_needs_service()


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(self._las)

    def spindler_needs_service(self):
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 2)
        return service_threshold_date < datetime.today().date()  # returns True if battery needs servicing


class NubbinBattery:
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def nubbin_needs_service(self):
        service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 4)
        return service_threshold_date < datetime.today().date()  # returns True if battery needs servicing
