from battery import *
from car import Car
from engine import *
import datetime

class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        """
        Creates a Calliope Model car - Capulet Engine and Spindler Battery. 
        """
        capulet = Engine.CapuletEngine(last_service_mileage, current_mileage)
        spindler = Battery.SpindlerBattery(last_service_date, current_date)
        calliope = Car(capulet, spindler)  # create a Car instance with Capulet + Spindler
        return calliope

    def create_glissade(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        """
        Creates a Glissade Model car - Willoughby Engine and Spindler Battery
        """
        willoughby = Engine.WilloughbyEngine(last_service_mileage, current_mileage)
        spindler = Battery.SpindlerBattery(last_service_date, current_date)
        glissade = Car(willoughby, spindler)  # create a Car instance with Willoughby + Spindler
        return glissade

    def create_palindrome(self, current_date, last_service_date, warning_light_on: bool) -> Car:
        """
        Creates a Palindrome Model car - Sternman Engine and Spindler Battery
        """
        sternman = Engine.SternmanEngine(warning_light_on)
        spindler = Battery.SpindlerBattery(last_service_date, current_date)
        palindrome = Car(sternman, spindler)  # create a Car instance with Sternman + Spindler
        return palindrome

    def create_rorscach(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        """
        Creates a Rorschach Model car - Willoughby Engine and Nubbin Battery
        """
        willoughby = Engine.WilloughbyEngine(last_service_mileage, current_mileage)
        nubbin = Battery.NubbinBattery(last_service_date, current_date)
        rorschach = Car(willoughby, nubbin)  # create a Car instance with Willoughby + Nubbin
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        """
        Creates a Thovex Model car - Capulet Engine and Nubbin Battery
        """
        capulet = Engine.CapuletEngine(last_service_mileage, current_mileage)
        nubbin = Battery.NubbinBattery(last_service_date, current_date)
        thovex = Car(capulet, nubbin)  # create a Car instance with Capulet + Nubbin
        return thovex

