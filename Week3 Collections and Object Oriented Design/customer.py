class Customer:

    def __init__(self, name, age):
        self.__name = name
        self.age = age
    
    def get_name(self):
        return self.__name