

class MovementSystem:
    def move_entity_to(self, entity, new_x, new_y):
        position = entity.get_component('position')
        if position:
            position.x = new_x
            position.y = new_y


