from ship import Ship

class Ocean:
    def __init__(self):
        self.shots_fired = 0
        self.hit_count = 0
        self.ships_sunk = 0

        self.ships = []
        for i in range(20):
            row = []
            for j in range (20):
                row.append(Ship())
            self.ships.append(row)
    
    def place_all_ships_randomly(self):
        pass

    def is_occupied(self, row, colum):
        pass

    def shot_at(self, row, column):
        pass

    def get_shots_fired(self):
        pass

    def get_hit_count(self):
        pass

    def get_ships_sunk(self):
        pass

    def is_gameover(self):
        pass

    def get_ship_array(self):
        pass

    def print(self):
        pass