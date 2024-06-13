import pygame
import os


def load_image(name):
    full_path = os.path.join('assets', 'tiles', name)
    return pygame.image.load(full_path)




water_img = load_image('water.png')
land_img = load_image('land.png')
land_grass_img = load_image('land_grass.png')
land_flowers_img = load_image('land_flowers.png')