
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


class VelocityComponent:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


class CityResourcesComponent:
    def __init__(self):
        self.resources = []


class RenderComponent:
    def __init__(self, image):
        self.image = image
