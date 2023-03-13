from hubs.simulated_hub.hub import SimulatedHub

class State:
    def __init__(self):
        self.hubs = {
            "simulated": SimulatedHub()
        }
