import pygame
from .ecs.entities.entities import SoldierEntity, TankEntity, CityEntity

# ВСЕ ЦИФРЫ СДЕЛАТЬ СТРОКАМИ
IMG_PATHS = {
    0: 'assets/tiles/terrain/water.png',
    1: 'assets/tiles/terrain/land.png',
    2: 'assets/tiles/terrain/land_grass.png',
    3: 'assets/tiles/terrain/land_flowers.png',

    4: 'assets/tiles/buildings/blue_factory.png',
    5: 'assets/tiles/buildings/red_factory.png',

    6: 'assets/tiles/units/blue_soldier.png',
    7: 'assets/tiles/units/blue_tank.png',
    8: 'assets/tiles/units/red_soldier.png',
    9: 'assets/tiles/units/red_tank.png',

    10: 'assets/tiles/other/cursor.png',
    11: 'assets/tiles/other/fuel.png',
    12: 'assets/tiles/other/money.png'
}

UNIT_IMAGES = {
    CityEntity: {0: 4, 1: 5},
    SoldierEntity: {0: 6, 1: 8},
    TankEntity: {0: 7, 1: 9}
}


def load_images() -> dict:
    return {key: pygame.image.load(path) for key, path in IMG_PATHS.items()}

