from ...assets_loader import UNIT_IMAGES
from ...ecs.entities.entities import CityEntity, SoldierEntity, TankEntity
from ...ecs.entity_creator import create_entity
from ...settings import *


class GameState:
    def __init__(self) -> None:
        self.__turn = 0
        self.__player_id = 0
        self.__turn_phase = 0
        self.player_entities_png = UNIT_IMAGES
        self.cities = {0: [], 1: []}
        self.entities = {0: [], 1: []}
        self.__production_queue = {0: {}, 1: {}}
        self.selected_unit = None

    def add_cities(self, generate_city_spawn: callable) -> None:
        blue_city_pos = generate_city_spawn((0, 0), (MAP_HEIGHT // 2, MAP_WIDTH // 2))
        red_city_pos = generate_city_spawn((MAP_HEIGHT // 2, MAP_WIDTH // 2), (MAP_HEIGHT - 1, MAP_WIDTH - 1))

        self._create_and_add_city(blue_city_pos, 0)
        self._create_and_add_city(red_city_pos, 1)

    def _create_and_add_city(self, city_pos, player_id: int) -> None:
        city = create_entity(city_pos[1], city_pos[0],
                             entity_color=self.get_entity_color_for_player(CityEntity, player_id),
                             entity=CityEntity, player_id=player_id)
        self.cities[player_id].append(city)

    def add_entity(self, entity) -> None:
        self.entities[self.__player_id].append(entity)

    def add_unit_to_production_queue(self, player_id: int, unit_type, production_time: int) -> None:
        self.__production_queue[player_id][unit_type] = production_time
        print(f'Юнит добавлен в очередь. Список юнитов: {self.__production_queue}')

    def process_production_queue(self) -> None:
        self.process_player_production_queue(BLUE_PLAYER)
        self.process_player_production_queue(RED_PLAYER)

    def process_player_production_queue(self, player_id: int) -> None:
        new_queue = {}
        for unit_type, turns_left in list(self.__production_queue[player_id].items()):
            if turns_left > 1:
                new_queue[unit_type] = turns_left - 1
            else:
                self.create_entity(unit_type, player_id)
        self.__production_queue[player_id] = new_queue

    def create_entity(self, unit_type, player_id: int) -> None:
        city = self.cities[player_id][0]
        city_position = city.get_component('position')
        new_unit = create_entity(city_position.x, city_position.y, player_id=player_id,
                                 entity_color=self.get_entity_color_for_player(unit_type, player_id), entity=unit_type)
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

    def get_current_turn(self) -> int:
        return self.__turn

    def get_entity_color_for_player(self, entity: CityEntity | SoldierEntity | TankEntity, player_id: int = None) -> int:
        if player_id is None:
            player_id = self.__player_id
        return self.player_entities_png.get(entity).get(player_id)

    def select_unit(self, unit):
        self.selected_unit = unit

    def deselect_unit(self):
        self.selected_unit = None

    def get_selected_unit(self):
        return self.selected_unit
