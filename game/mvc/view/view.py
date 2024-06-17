import pygame

from ...assets_loader import load_images
from ...settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR
from ...settings import TILE_SIZE

class View:
    def __init__(self):
        pygame.init()
        game_icon = next(iter(load_images().values()))  # заменить на какую-то другую иконку не забыть
        pygame.display.set_icon(game_icon)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pixel Commander')
        self.IMAGES = load_images()

    def draw_map(self, game_map):
        self.screen.fill(BG_COLOR)
        for row in range(len(game_map)):
            for col in range(len(game_map[0])):
                tile_value = game_map[row][col]
                tile_image = self.IMAGES[tile_value]
                self.screen.blit(tile_image, (col * TILE_SIZE, row * TILE_SIZE))

        pygame.display.flip()
