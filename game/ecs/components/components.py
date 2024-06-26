
class PlayerComponent:
    def __init__(self, player_id: int) -> None:
        self.player_id: int = player_id


class PositionComponent:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class HealthComponent:
    def __init__(self, health: int) -> None:
        self.health: int = health


class VelocityComponent:
    def __init__(self, max_movement_range=3):
        self.max_movement_range = max_movement_range
        self.current_movement_range = max_movement_range

    def reset_movement_range(self):
        self.current_movement_range = self.max_movement_range

    def use_movement(self, distance):
        if distance <= self.current_movement_range:
            self.current_movement_range -= distance
            return True
        return False



class CityResourcesComponent:
    def __init__(self):
        self.resources = []


class RenderComponent:
    def __init__(self, image):
        self.image = image
