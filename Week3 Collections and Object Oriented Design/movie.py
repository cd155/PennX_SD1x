class Movie:

    def __init__(self, name, rating = None):
        self.__name = name
        self.__rating = rating
        self.__actors = []


    def get_movie_name(self):
        return self.__name

    def get_actors(self):
        return self.__actors

    def get_rating(self):
        return self.__rating

    def set_movie_name(self, new_name):
        self.__name = new_name

    def set_actors(self, actors):
        self.__actors = actors

    def set_rating(self, new_rating):
        self.__rating = new_rating