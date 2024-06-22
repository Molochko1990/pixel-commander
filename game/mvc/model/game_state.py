import random

from ...ecs.entity_creator import create_soldier, create_city
from ...settings import *


class GameState:
    def __init__(self) -> None:
        # сделать отдельные очереди для обоих игроков
        self.turn = 0
        self.player_id = 0  # 0 - первый игрок, 1 - второй игрок
        self.cities = []
        self.entities = []
        self.entity_counter = 0
        self.production_queue = {0: [], 1: []}

    def add_cities(self, game_map: list[list[int]]) -> None:
        half_width = MAP_WIDTH // 2
        half_height = MAP_HEIGHT // 2

        def generate_city_spawn(top_left: tuple[int, int], bottom_right: tuple[int, int]) -> tuple[int, int]:
            while True:
                row = random.randint(top_left[0], bottom_right[0])
                col = random.randint(top_left[1], bottom_right[1])
                if game_map[row][col] == LAND:
                    print(f"Selected land tile at ({row}, {col}) with value {game_map[row][col]}")
                    return (row, col)

        city1_pos = generate_city_spawn((0, 0), (half_height, half_width))
        city2_pos = generate_city_spawn((half_height, half_width), (MAP_HEIGHT - 1, MAP_WIDTH - 1))

        first_city = create_city(city1_pos[1],city1_pos[0], player_color=4)
        second_city = create_city(city2_pos[1],city2_pos[0], player_color=5)

        self.cities.append(first_city)
        self.cities.append(second_city)


    def add_entity(self, entity) -> None:
        self.entities.append(entity)

    def add_unit_to_production_queue(self, player_id: int, unit_type: str, production_time: int) -> None:
        self.production_queue[player_id].append((unit_type, production_time))
        print(f'юнит добавлен в очередь. кол-во юнитов там {self.entities}')  # УБРАТЬ ЭТО

    def process_production_queue(self) -> None:
        for player_id in [0, 1]:
            new_queue: list[tuple[str, int]] = []
            for unit_type, turns_left in self.production_queue[player_id]:
                if turns_left > 1:
                    new_queue.append((unit_type, turns_left - 1))
                else:
                    self.create_unit(player_id, unit_type)
            self.production_queue[player_id] = new_queue

    def create_unit(self, player_id: int, unit_type: str) -> None:
        if unit_type == "Солдат":
            new_unit = create_soldier()
        # elif unit_type == "Танк":
        #     new_unit = create_tank(player_id)
        self.add_entity(new_unit)

    def next_turn(self) -> None:
        self.turn += 1
        self.player_id = (self.player_id + 1) % 2

    def get_current_player(self) -> int:
        return self.player_id
