from modules.module_templates.sensor_class import SensorClass


class DummySensor(SensorClass):

    def __init__(self, pin):
        self.pin = pin

    def get_state(self):
        return {
            'temp': 1.0
        }
