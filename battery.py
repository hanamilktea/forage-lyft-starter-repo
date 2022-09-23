from datetime import datetime
from car import *


class Battery:
    """
    Constructor representing Battery service criteria of the Car object.
    Depending on type of battery, determines if the car needs to be serviced.
    """

    class SpindlerBattery:
        def __init__(self, last_service_date, current_date):
            self._last_service_date = last_service_date
            self._current_date = current_date

        def battery_needs_service(self) -> bool:
            spindler_service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 2)
            return spindler_service_threshold_date < datetime.today().date()

    class NubbinBattery:
        def __init__(self, last_service_date, current_date):
            self._last_service_date = last_service_date
            self._current_date = current_date

        def battery_needs_service(self) -> bool:
            nubbin_service_threshold_date = self._last_service_date.replace(year=self._last_service_date.year + 4)
            return nubbin_service_threshold_date < datetime.today().date()