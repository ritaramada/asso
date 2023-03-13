from devices.device import Device
from components.switch import Switch

class LightSwitch(Switch):
    def turn_on(self):
        return { "state": "true" }
    def turn_off(self):
        return { "state": "false" }


# def create_light():
#     device = Device()
#     device.register_component(Switch, LightSwitch)
#     return device
