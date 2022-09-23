from CarFactory import *


class Engine:
    """
    Constructor representing the Engine service criteria for a Car object.
    Determines if the car needs to be serviced depending on the type of Engine. 
    """

    class CapuletEngine:
        def __init__(self, last_service_mileage, current_mileage):
            self._last_service_mileage = last_service_mileage
            self._current_mileage = current_mileage

        def engine_needs_service(self) -> bool:
            # needs service after 30k miles
            return self._current_mileage - self._last_service_mileage > 30000

    class WilloughbyEngine:
        def __init__(self, last_service_mileage, current_mileage):
            self._last_service_mileage = last_service_mileage
            self._current_mileage = current_mileage

        def engine_needs_service(self) -> bool:
            # needs service after 60k miles
            return self._current_mileage - self._last_service_mileage > 60000

    class SternmanEngine:
        def __init__(self, warning_light_on=False):
            self._warning_light_on = warning_light_on

        def engine_needs_service(self) -> bool:
            # needs service when warning light on
            return self._warning_light_on
