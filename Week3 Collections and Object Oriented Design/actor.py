class Actor:

    def __init__(self, name, movies=[]) -> None:
        self.__name = name
        self.__movies = movies

    def get_actor_name(self):
        return self.__name

    def set_actor_name(self, new_name):
        self.__name = new_name
    
    def get_movies(self):
        return self.__movies
