from modules.module_templates.switch_class import SwitchClass


class GPIORelay(SwitchClass):

    def __init__(self, pin):
        self.pin = pin
        self.state = False

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
