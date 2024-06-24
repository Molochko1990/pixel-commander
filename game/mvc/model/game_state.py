import random


from ...assets_loader import UNIT_IMAGES
from ...ecs.entities.entities import CityEntity, SoldierEntity, TankEntity
from ...ecs.entity_creator import create_entity
from ...settings import *


class GameState:
    def __init__(self) -> None:
        # сделать отдельные очереди для обоих игроков
        self.__turn = 0
        self.__player_id = 0  # 0 - первый игрок, синий; 1 - второй игрок, красный
        self.__turn_phase = 0
        self.player_entities_png = UNIT_IMAGES
        self.cities = {}
        self.entities = {}
        self.entity_counter = 0
        self.production_queue = {0: {}, 1: {}}

    def add_cities(self, generate_city_spawn: callable) -> None:
        half_width = MAP_WIDTH // 2
        half_height = MAP_HEIGHT // 2

        blue_city_pos = generate_city_spawn((0, 0), (half_height, half_width))
        red_city_pos = generate_city_spawn((half_height, half_width), (MAP_HEIGHT - 1, MAP_WIDTH - 1))

        blue_city = create_entity(blue_city_pos[1], blue_city_pos[0],
                                  entity_color=self.get_entity_color_for_player(CityEntity),
                                  entity=CityEntity)
        red_city = create_entity(red_city_pos[1], red_city_pos[0],
                                 entity_color=self.get_entity_color_for_player(CityEntity)+1,
                                 entity=CityEntity)

        self.cities[self.__player_id] = blue_city
        self.cities[self.__player_id + 1] = red_city

    def add_entity(self, entity) -> None:
        self.entities[self.__player_id] = entity

    def add_unit_to_production_queue(self, player_id: int, unit_type, production_time: int) -> None:
        self.production_queue[player_id][unit_type] = production_time
        print(f'юнит добавлен в очередь. кол-во юнитов там {self.entities}')  # УБРАТЬ ЭТО

    def process_production_queue(self) -> None:
        self.process_player_production_queue(self.__player_id)
        self.process_player_production_queue((self.__player_id + 1) % 2)

    def process_player_production_queue(self, player_id: int) -> None:
        new_queue = {}
        for unit_type, turns_left in list(self.production_queue[player_id].items()):
            print(turns_left)
            if turns_left > 1:
                new_queue[unit_type] = turns_left - 1
            else:
                self.create_entity(unit_type, player_id)
        self.production_queue[player_id] = new_queue

    def create_entity(self, unit_type, player_id: int) -> None:
        new_unit = create_entity(x=50, y=50, entity_color=self.get_entity_color_for_player(unit_type, player_id), entity=unit_type)
        self.add_entity(new_unit)

    def next_turn(self) -> None:
        if self.__turn_phase == 0:
            self.__turn_phase = 1
            self.__turn += 1
            self.__player_id = (self.__player_id + 1) % 2
        else:
            self.process_production_queue()
            self.__turn_phase = 0
            self.__turn += 1
            self.__player_id = (self.__player_id + 1) % 2
        print(f'Ход {self.__player_id}-го игрока')

    def get_current_player(self) -> int:
        return self.__player_id


    def get_entity_color_for_player(self, entity: CityEntity | SoldierEntity | TankEntity, player_id: int = None) -> int:
        if player_id is None:
            player_id = self.__player_id
        return self.player_entities_png.get(entity).get(player_id)
