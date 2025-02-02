from abc import ABC, abstractmethod
from battery import *
from engine import *
from CarFactory import *


class Car:
    def __init__(self, engine, battery):
        self._engine = engine
        self._battery = battery

    def needs_service(self) -> bool:
        # whether car needs to be serviced - depends on battery and engine
        # Component needs to be easily modified so that new service criteria can be quickly added/updated
        if self._battery.battery_needs_service or self._engine.engine_needs_service:
            return True
