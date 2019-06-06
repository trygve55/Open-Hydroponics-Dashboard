from modules.module_templates.sensor_class import SensorClass
import Adafruit_DHT
import threading
import time


def thread_sensor(tmp, hum):
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.pin)

        print(temperature, " ", humidity)

        print(tmp, " ", hum)

        if humidity is not None and temperature is not None:
            print("test")
            hum = humidity
            tmp = temperature
        time.sleep(3)


class AM2302(SensorClass):

    def __init__(self, pin):
        self.pin = pin
        self.temperature = 0.0
        self.humidity = 0.0

        x = threading.Thread(target=thread_sensor, args=(self.temperature, self.humidity))
        x.start()

    def get_state(self):
        return {
            "humidity": self.humidity,
            "temperature": self.temperature
        }


