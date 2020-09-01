from ship import Ship

class EmptySea(Ship):

    def __init__(self):
        self.length = 1

    def shoot_at(self, row, column):
        return False

    def is_sunk():
        return False

    def __str__(self):
        return "e"

    def get_ship_type(self):
        return "empty"