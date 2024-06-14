
class PlayerComponent:
    def __init__(self, name):
        self.player_name = name


class PositionComponent:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class HealthComponent:
    pass


class MovementComponent:
    pass


class CityComponent:
    def __init__(self):
        self.resources = []