from modules.module_templates.sensor_class import SensorClass
import Adafruit_DHT
import threading
import time


def thread_sensor(self):
    self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.pin)
    time.sleep(3)


class AM2302(SensorClass):

    def __init__(self, pin):
        self.pin = pin
        self.temperature = 0.0
        self.humidity = 0.0

        threading.Thread(target=thread_sensor, args=(self,))

    def get_state(self):
        return {
            "humidity": self.humidity,
            "temperature": self.temperature
        }


