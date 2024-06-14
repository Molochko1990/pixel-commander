import pygame

from ..assets_loader import water_img
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR
from ..map_generator import MapGenerator
from ..settings import TILE_SIZE

class View:
    def __init__(self):
        pygame.init()
        game_icon = water_img  # заменить на какую-то другую иконку не забыть
        pygame.display.set_icon(game_icon)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Pixel Commander')

    # def draw_map(self, game_map):
    #     self.screen.fill(BG_COLOR)
    #     for row in game_map:
    #         for tile in row:
    #             self.screen.blit(tile.image, tile.rect)

        # for city in cities:
        #     pos = city.get_component('position')
        #     self.screen.blit(city.image, (pos.x, pos.y))
        # pygame.display.flip()


    def draw_map(self, game_map):
        self.screen.fill(BG_COLOR)
        for row in range(len(game_map)):
            for col in range(len(game_map[row])):
                self.screen.blit(game_map[row][col], (col * TILE_SIZE, row * TILE_SIZE))

        pygame.display.flip()