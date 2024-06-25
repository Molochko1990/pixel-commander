import math
from ..components.components import PositionComponent, VelocityComponent


class MovementSystem:
    def __init__(self, game_map):
        self.game_map = game_map

    def move_unit(self, entity, dx, dy):
        pos = entity.get_component(PositionComponent)
        vel = entity.get_component(VelocityComponent)

        if not pos or not vel:
            return

        new_x = pos.x + dx
        new_y = pos.y + dy

        if (0 <= new_x < len(self.game_map[0]) and 0 <= new_y < len(self.game_map) and self.game_map[new_y][new_x] != 0):
            pos.x = new_x
            pos.y = new_y

    def update(self, entities):
        for entity in entities:
            if isinstance(entity, Tank):
                self.move_unit(entity, entity.dx, entity.dy, 4)
            elif isinstance(entity, Soldier):
                self.move_unit(entity, entity.dx, entity.dy, 2)


class Tank:
    def __init__(self):
        self.position = PositionComponent(0, 0)
        self.velocity = VelocityComponent(0, 0)
        self.movement_range = 4

    def get_component(self, component_class):
        if component_class == PositionComponent:
            return self.position
        elif component_class == VelocityComponent:
            return self.velocity
        return None


class Soldier:
    def __init__(self):
        self.position = PositionComponent(0, 0)
        self.velocity = VelocityComponent(0, 0)
        self.movement_range = 2

    def get_component(self, component_class):
        if component_class == PositionComponent:
            return self.position
        elif component_class == VelocityComponent:
            return self.velocity
        return None
