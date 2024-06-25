# systems.py

class MovementSystem:
    def move_unit(self, unit, position):
        if self.can_move(unit, position):
            unit.position = position

    def can_move(self, unit, position):
        pass