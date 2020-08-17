class Actor:

    def __init__(self, name):
        self.__name = name
        self.__movies = []

    def get_actor_name(self):
        return self.__name
    
    def get_movies(self):
        return self.__movies

    def set_actor_name(self, new_name):
        self.__name = new_name

    def set_movies(self, new_movies):
        self.__movies = new_movies
