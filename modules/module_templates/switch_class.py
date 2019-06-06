from abc import ABC, abstractmethod


class SwitchClass(ABC):

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass
