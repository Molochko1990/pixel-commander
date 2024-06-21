class BaseEntity:
    def __init__(self):
        self.components = {}

    def add_component(self, component_type, component_value):
        self.components[component_type] = component_value

    def get_component(self, component_type):
        return self.components.get(component_type)


class CityEntity(BaseEntity):
    pass


class SoldierEntity(BaseEntity):
    pass


class TankEntity(BaseEntity):
    pass


