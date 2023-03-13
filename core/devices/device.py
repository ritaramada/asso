class Device:
    def __init__(self):
        self._components = {}

    def get_components(self): 
        return self._components
    
    def register_component(self, type, obj):
        self._components[type] = obj
