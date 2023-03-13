import requests
from hubs.hub import Hub
from uuid import uuid4
from components.switch import Switch
from hubs.simulated_hub.light import LightSwitch
from devices.device import Device
import json

"""
    {
        device_id: 
        request: 
    }
"""

ON = "on"
OFF = "off"

devices = {
    "light": [Switch, LightSwitch()]
}

class SimulatedHub(Hub):
    def __init__(self):
        self._devices = {}

    def get_devices(self):
        return self._devices
    
    def get_device_id(self, device_path):
        found_devices = list(filter(lambda reg: reg[1]["device_path"] == device_path, self._devices.items()))
        id_list = [x for x in map(lambda dev: dev[0], found_devices)]
        return id_list[0] if len(id_list) > 0 else -1

    def _add_device(self, device, device_path):
        # found_devices = list(filter(lambda reg: reg[1]["device_path"] == device_path, self._devices.items()))
        # if not any(found_devices):
        device_id = self.get_device_id(device_path)
        print(device_id)
        if device_id == -1:
            new_id = uuid4()
            self._devices[new_id] = {
                "device_path": device_path,
                "device": device
            }
            return new_id
        return device_id

    def connect(self, device_path):
        r_json = requests.get(device_path).json()
        device_components = devices[r_json["type"]]
        if device_components:
            device = Device()
            device.register_component(device_components[0], device_components[1])
            return self._add_device(device, device_path)
    
    def turn(self, device_path, switch_state):
        r_json = requests.get(device_path).json()
        device_components = devices[r_json["type"]]
        if device_components:
            # TODO: Check if device id already exists
            device = self._devices[self.get_device_id(device_path)]['device']
            if (switch_state == "on"):
                state = device.get_components()[Switch].turn_on()
            else:
                state = device.get_components()[Switch].turn_off()
            return requests.post(device_path + '/' + r_json["type"], json.dumps(state)).json()

    def turn_on(self, device_path):
        return self.turn(device_path, ON)
        
    def turn_off(self, device_path):
        return self.turn(device_path, OFF)
            

