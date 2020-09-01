from abc import ABC, abstractmethod, abstractproperty

class Ship(ABC):
    @property
    @abstractmethod
    def bow_row(self):
        pass

    @property
    @abstractmethod
    def bow_column(self):
        pass

    @property
    @abstractmethod    
    def length(self):
        pass
    
    @property
    @abstractmethod
    def horizontal(self):
        pass

    @property
    @abstractmethod
    def hit(self):
        pass

    @abstractmethod
    def get_ship_type(self):
        raise NotImplementedError

    def ok_to_place_ship_at(self, row, column, horizontal, ocean):
        raise NotImplementedError

    def place_ship_at(self, row, column, horizontal, ocean):
        raise NotImplementedError

    def shoot_at(self, row, column):
        raise NotImplementedError

    def is_sunk(self):
        raise NotImplementedError

    def __str__(self):
        if self.is_sunk():
            return "x"
        else:
            return "S"
            