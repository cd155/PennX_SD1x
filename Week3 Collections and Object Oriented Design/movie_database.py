class MovieDatabase:

    def __init__(self):
        self.__moive_list = []
        self.__actor_list = []
    
    def get_movie_list(self):
        return self.__moive_list
    
    def get_actor_list(self):
        return self.__actor_list
    
    def add_movie(self, movie_name, actors):
        pass

    def add_rating(self, movie_name, rating):
        pass

    def update_rating(self, movie_name, new_rating):
        pass

    def get_best_actor(self):
        pass

    def get_best_movie(self):
        pass