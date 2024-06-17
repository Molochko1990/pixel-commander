import pygame


IMG_PATHS = {
    0: 'assets/tiles/terrain/water.png',
    1: 'assets/tiles/terrain/land.png',
    2: 'assets/tiles/terrain/land_grass.png',
    3: 'assets/tiles/terrain/land_flowers.png',

    4: 'assets/tiles/buildings/blue_factory.png',
    5: 'assets/tiles/buildings/red_factory.png'
}


def load_images():
    return {key: pygame.image.load(path) for key, path in IMG_PATHS.items()}
