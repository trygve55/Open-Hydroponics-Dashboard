from modules.module_templates.sensor_class import SensorClass
import RPi.GPIO as GPIO


class GPIODigitalInput(SensorClass):

    def __init__(self, pin):
        self.pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get_state(self):
        return GPIO.input(self.pin)
