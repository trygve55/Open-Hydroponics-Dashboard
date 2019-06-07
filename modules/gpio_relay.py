from modules.module_templates.switch_class import SwitchClass
import RPi.GPIO as GPIO


class GPIORelay(SwitchClass):

    def __init__(self, pin):
        self.pin = pin
        self.state = 0

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    def get_state(self):
        return self.state

    def set_state(self, state):
        if self.state == state:
            return

        GPIO.output(self.pin, state)
        self.state = state
