from modules.module_templates.sensor_class import SensorClass
import Adafruit_DHT
import threading
import time


def thread_sensor(self):
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.pin)

        print(temperature, " ", humidity)

        if humidity is not None and temperature is not None:
            self.humidity = humidity
            self.temperature = temperature
        time.sleep(3)


class AM2302(SensorClass):

    def __init__(self, pin):
        self.pin = pin
        self.temperature = 0.0
        self.humidity = 0.0

        x = threading.Thread(target=thread_sensor, args=(self,))
        x.start()

    def get_state(self):
        return {
            "humidity": self.humidity,
            "temperature": self.temperature
        }


