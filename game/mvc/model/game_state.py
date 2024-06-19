from ecs.entity_factory.py import create_soldier, create_city

class GameState:
    def __init__(self):
        self.turn = 0  # 0 - первый игрок, 1 - второй игрок
        self.entities = []
        self.entity_counter = 0
        self.init_entities()

    def init_cities(self):
        pass



    def next_turn(self):
        self.turn = (self.turn + 1) % 2

    def get_current_player(self):
        return self.turn
