# systems.py

class MovementSystem:
    def __init__(self, game_state):
        self.game_state = game_state

    def move_entity(self, entity, move_target):
        velocity_component = entity.get_component('velocity')
        position_component = entity.get_component('position')
        player_component = entity.get_component('player_id')
        if player_component.player_id != self.game_state.get_current_player():
            print(f"Cannot move entity, it belongs to player {player_component.player_id}")
            return False
        if velocity_component and position_component:
            distance = self.calculate_distance((position_component.x, position_component.y), move_target)
            if distance <= velocity_component.max_movement_range:
                if velocity_component.use_movement(distance):
                    position_component.x, position_component.y = move_target
                    return True
        return False

    def calculate_distance(self, start_pos, end_pos):
        return abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
