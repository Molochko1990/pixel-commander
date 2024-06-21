from ...ecs.entity_creator import create_soldier

class GameState:
    def __init__(self):
        self.turn = 0
        self.player_id = 0  # 0 - первый игрок, 1 - второй игрок
        self.entities = []
        self.entity_counter = 0
        self.production_queue = {0: [], 1: []}

    def add_entity(self, entity):
        self.entities.append(entity)
        self.entity_counter += 1

    def add_unit_to_production_queue(self, player_id, unit_type, production_time):
        self.production_queue[player_id].append((unit_type, production_time))

    def process_production_queue(self):
        for player_id in [0, 1]:
            new_queue = []
            for unit_type, turns_left in self.production_queue[player_id]:
                if turns_left > 1:
                    new_queue.append((unit_type, turns_left - 1))
                else:
                    self.create_unit(player_id, unit_type)
            self.production_queue[player_id] = new_queue

    def create_unit(self, player_id, unit_type):
        if unit_type == "Солдат":
            new_unit = create_soldier()
        # elif unit_type == "Танк":
        #     new_unit = create_tank(player_id)
        self.add_entity(new_unit)

    def next_turn(self):
        self.turn += 1
        self.player_id = (self.player_id + 1) % 2

    def get_current_player(self):
        return self.player_id
