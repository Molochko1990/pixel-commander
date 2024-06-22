class BaseEntity:
    def __init__(self) -> None:
        self.components: dict[str, any] = {}

    def add_component(self, component_type: str, component_value: any) -> None:
        self.components[component_type] = component_value

    def get_component(self, component_type: str) -> any:
        return self.components.get(component_type)


class CityEntity(BaseEntity):
    pass


class SoldierEntity(BaseEntity):
    pass


class TankEntity(BaseEntity):
    pass


