
class PlayerComponent:
    def __init__(self, name):
        self.player_name = name


class PositionComponent:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class HealthComponent:
    def __init__(self, health):
        self.health = health


class MovementComponent:
    def __init__(self, movement_range):
        self.movement_range = movement_range


class CityComponent:
    def __init__(self):
        self.resources = []


class RenderComponent:
    def __init__(self, image):
        self.image = image
