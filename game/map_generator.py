import random
from .settings import TILE_SIZE, MAP_WIDTH, MAP_HEIGHT, BORDER_SIZE, LAND_PROBABILITY
from .assets_loader import *


class MapGenerator:
    def __init__(self):
        self.__tile_size = TILE_SIZE
        self.__map_width = MAP_WIDTH
        self.__map_height = MAP_HEIGHT
        self.__border_size = BORDER_SIZE
        self.__land_probability = LAND_PROBABILITY
        self.__map = self.generate_world(self.__map_width, self.__map_height, land_probability= self.__land_probability, border_size=self.__border_size)

    def smooth_map(self):
        land_tiles = [land_img, land_grass_img, land_flowers_img]
        weights = [70, 90, 10]
        for row in range(self.__map_height):
            for col in range(self.__map_width):
                land_neighbors = self.count_land_neighbors(row, col)
                if self.__map[row][col] != water_img and land_neighbors < 4:
                    self.__map[row][col] = water_img
                elif self.__map[row][col] == water_img and land_neighbors > 4:
                    self.__map[row][col] = random.choices(land_tiles, weights=weights, k=1)[0]

    def count_land_neighbors(self, row, col):
        land_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_row = row + i
                neighbor_col = col + j
                if (i != 0 or j != 0) and (0 <= neighbor_row < self.__map_height) and (0 <= neighbor_col < self.__map_width):
                    if self.__map[neighbor_row][neighbor_col] != water_img:
                        land_neighbors += 1
        return land_neighbors

    # переделать это все
    # def add_shores(self):
    #     for row in range(self.__map_height):
    #         for col in range(self.__map_width):
    #             if self.__map[row][col] == 1 and self.has_water_neighbor(row, col):
    #                 self.__map[row][col] = 2  # 2 - берег

    def has_water_neighbor(self, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_row = row + i
                neighbor_col = col + j
                if (i != 0 or j != 0) and (0 <= neighbor_row < self.__map_height) and (
                        0 <= neighbor_col < self.__map_width):
                    if self.__map[neighbor_row][neighbor_col] == water_img:
                        return True
        return False

    def generate_world(self, width: int, height: int, land_probability: float, border_size: int):
        self.__map = [[water_img for _ in range(width)] for _ in range(height)]
        for row in range(height):
            for col in range(width):
                if row >= border_size and row < height - border_size and col >= border_size and col < width - border_size:
                    if random.random() < land_probability:
                        self.__map[row][col] = land_img
        self.smooth_map()
        # self.add_shores()
        return self.__map

    def get_map(self):
        return self.__map

    def draw_map(self, screen):
        for row in range(len(self.__map)):
            for col in range(len(self.__map[row])):
                screen.blit(self.__map[row][col], (col * TILE_SIZE, row * TILE_SIZE))

