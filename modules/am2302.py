from modules.module_templates.sensor_class import SensorClass
import Adafruit_DHT

class AM2302(SensorClass):

    def __init__(self, pin):
        self.pin = pin

    def get_state(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.pin)
        return {
            "humidity": humidity,
            "temperature": temperature
        }
