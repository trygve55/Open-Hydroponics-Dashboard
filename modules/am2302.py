from modules.module_templates.sensor_class import SensorClass
import Adafruit_DHT
import threading
import time


def thread_sensor(test2):
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, test2.pin)

        print(temperature, " ", humidity)

        print(test2.temperature, " ", test2.humidity)

        if humidity is not None and temperature is not None:
            print("test")
            test2.humidity = humidity
            test2.temperature = temperature

            print(test2.temperature, " ", test2.humidity)
        time.sleep(3)


class AM2302(SensorClass):

    def __init__(self, pin):
        self.pin = pin
        self.temperature = 0.0
        self.humidity = 0.0

        x = threading.Thread(target=thread_sensor, args=(self,))
        x.start()

    def get_state(self):
        print(self.temperature, " ", self.humidity)
        return {
            "humidity": self.humidity,
            "temperature": self.temperature
        }


