import pygame
import os


def load_image(name):
    return pygame.image.load(name)


# terrain
water_img = load_image('assets/tiles/terrain/water.png')
land_img = load_image('assets/tiles/terrain/land.png')
land_grass_img = load_image('assets/tiles/terrain/land_grass.png')
land_flowers_img = load_image('assets/tiles/terrain/land_flowers.png')

# buildings
blue_factory = load_image('assets/tiles/buildings/blue_factory.png')
red_factory = load_image('assets/tiles/buildings/red_factory.png')
