# Screen size
SCREEN_WIDTH = 1280  # 1280 1920 2560
SCREEN_HEIGHT = 720  # 720 1080 1440

# Map settings
MAP_WIDTH = SCREEN_WIDTH // 16
MAP_HEIGHT = SCREEN_HEIGHT // 16
BORDER_SIZE = 5  # кол-во обязательных тайлов воды на краю игрового поля
LAND_PROBABILITY = 0.6  # вероятность появления тайла земли

# Other
TILE_SIZE = 16
BG_COLOR = (0, 0, 0)

# Tile ids
WATER = 0
LAND = 1
LAND_GRASS = 2
LAND_FLOWERS = 3

# Player colors
BLUE_PLAYER = 0
RED_PLAYER = 1

# unit creation time
unit_creation_time = {"soldier": 1, "tank": 2}  # кол-во ходов для производства юнита
