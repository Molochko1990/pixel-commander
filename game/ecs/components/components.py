
class PlayerComponent:
    def __init__(self, name: str) -> None:
        self.player_name: str = name


class PositionComponent:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class HealthComponent:
    def __init__(self, health: int) -> None:
        self.health: int = health


class VelocityComponent:
    def __init__(self, dx: int, dy: int) -> None:
        self.dx: int = dx
        self.dy: int = dy


class CityResourcesComponent:
    def __init__(self):
        self.resources = []


class RenderComponent:
    def __init__(self, image):
        self.image = image
