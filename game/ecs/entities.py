class BaseEntity:
    def __init__(self, entity_id):
        self.id = entity_id
        self.components = {}

    def add_component(self, component_type, component_value):
        self.components[component_type] = component_value

    def get_component(self, component_type):
        return self.components.get(component_type)


class PlayerEntity(BaseEntity):
    pass


class CityEntity(BaseEntity):
    pass


class SoldierEntity(BaseEntity):
    pass
