import random
from ...settings import *


class MapGenerator:
    def __init__(self):
        self.__map_width = MAP_WIDTH
        self.__map_height = MAP_HEIGHT
        self.__border_size = BORDER_SIZE
        self.__land_probability = LAND_PROBABILITY
        self.__map = self.__generate_world(self.__map_width, self.__map_height, land_probability=self.__land_probability, border_size=self.__border_size)

    def __smooth_map(self):
        land_tiles = [LAND, LAND_GRASS, LAND_FLOWERS]
        weights = [70, 90, 10]
        for row in range(self.__map_height):
            for col in range(self.__map_width):
                land_neighbors = self.__count_land_neighbors(row, col)
                if self.__map[row][col] != WATER and land_neighbors < 4:
                    self.__map[row][col] = WATER
                elif self.__map[row][col] == WATER and land_neighbors > 4:
                    self.__map[row][col] = random.choices(land_tiles, weights=weights, k=1)[0]

    def __count_land_neighbors(self, row, col):
        land_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_row = row + i
                neighbor_col = col + j
                if (i != 0 or j != 0) and (0 <= neighbor_row < self.__map_height) and (0 <= neighbor_col < self.__map_width):
                    if self.__map[neighbor_row][neighbor_col] != WATER:
                        land_neighbors += 1
        return land_neighbors

    # def add_shores(self):
    #     pass

    def __has_water_neighbor(self, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_row = row + i
                neighbor_col = col + j
                if (i != 0 or j != 0) and (0 <= neighbor_row < self.__map_height) and (0 <= neighbor_col < self.__map_width):
                    if self.__map[neighbor_row][neighbor_col] == WATER:
                        return True
        return False

    def __generate_world(self, width: int, height: int, land_probability: float, border_size: int):
        self.__map = [[WATER for _ in range(width)] for _ in range(height)]
        for row in range(height):
            for col in range(width):
                if row >= border_size and row < height - border_size and col >= border_size and col < width - border_size:
                    if random.random() < land_probability:
                        self.__map[row][col] = LAND
        self.__smooth_map()
        # self.add_shores() доделать если успею
        # self.add_cities() переделать и удалить отсюда
        return self.__map



    def get_map(self):
        return self.__map

