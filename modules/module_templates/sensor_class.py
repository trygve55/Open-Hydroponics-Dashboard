from abc import ABC, abstractmethod


class SensorClass(ABC):

    @abstractmethod
    def get_state(self):
        pass
