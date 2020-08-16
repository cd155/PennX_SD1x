from movie import Movie
from actor import Actor

class MovieDatabase:

    def __init__(self):
        self.__moive_list = []
        self.__actor_list = []
    
    def get_movie_list(self):
        return self.__moive_list
    
    def get_actor_list(self):
        return self.__actor_list
    
    def add_movie(self, movie_name, actors):
        is_existed_movie = False
        for name in self.__moive_list:
            if name == movie_name:
                is_existed_movie = True
        
        if not is_existed_movie:
            self.__moive_list.append(movie_name)

        for new_actor in actors:
            is_existed_actor = False
            for actor in self.__actor_list:
                if new_actor == actor:
                    is_existed_actor = True

            if not is_existed_actor:
                self.__actor_list.append(new_actor)

    # we can combine add_rating and updating rating, because they shared the same logic
    def add_and_update_rating(self, name, rating):
        for movie in self.__moive_list:
            if movie.__name == name:
                movie.__rating = rating

    def get_best_actor(self):
        best_actor = None
        best_rating = 0
        for actor in self.__actor_list:
            current_rating = 0
            movies = actor.get_movies()
            for movie in movies:
                current_rating += movie.get_rating()
            current_rating = current_rating/len(movies)

            if best_rating < current_rating:
                best_actor = actor
                best_rating = current_rating
        return best_actor

    def get_best_movie(self):
        best_moive = None
        best_rating = 0
        for movie in self.__moive_list:
            if best_rating < movie.get_rating :
                best_moive = movie
                best_rating = movie.get_rating()
        return best_moive

# read text line by line
lines =[]
with open("Week3 Collections and Object Oriented Design/movies.txt") as filepath:
    lines = filepath.readlines()

total_actor_list = []
total_movie_list = []
for line in lines:
    content = line.split(",")
    movie_database = MovieDatabase()
    actor_movie_list = []
    for i in range(1, len(content)):
        movie = Movie(name=content[i])

        # be careful whether this can find duplicate movie
        if movie not in total_movie_list:
            total_movie_list.append(movie)
        else:
            print(movie)
        actor_movie_list.append(movie)
    total_actor_list.append(Actor(name=content[0], movies=actor_movie_list))

# movie add actor
for actor in total_actor_list:
    for movie in actor.get_movies():
        current_actors = movie.get_actors()
        current_actors.append(actor)