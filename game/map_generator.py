import random
from .settings import TILE_SIZE, MAP_WIDTH, MAP_HEIGHT


class MapGenerator:
    def __init__(self):
        self.__tile_size = TILE_SIZE
        self.__map_width = MAP_WIDTH
        self.__map_height = MAP_HEIGHT
        self.__map = self.generate_map(self.__map_width, self.__map_height)

    def generate_map(self, width, height, land_probability=0.8):
        # 0 - вода, 1 - суша
        return [[1 if random.random() < land_probability else 0 for _ in range(width)] for _ in range(height)]

    def get_map(self):
        return self.__map


    # def draw_map(self, screen):
    #     for row in range(len(MAP_DATA)):
    #         for col in range(len(MAP_DATA[row])):
    #             if MAP_DATA[row][col] == 0:
    #                 screen.blit(water_img, (col * TILE_SIZE, row * TILE_SIZE))
    #             elif MAP_DATA[row][col] == 1:
    #                 screen.blit(land_img, (col * TILE_SIZE, row * TILE_SIZE))
