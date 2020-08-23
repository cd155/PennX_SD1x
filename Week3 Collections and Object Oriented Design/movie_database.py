from movie import Movie
from actor import Actor

class MovieDatabase:

    def __init__(self):
        self.__movie_list = []
        self.__actor_list = []
    
    def get_movie_list(self):
        return self.__movie_list
    
    def get_actor_list(self):
        return self.__actor_list
    
    def add_movie(self, movie_name, actors):
        # find whether movie name exist in movie list
        target_moive = next((x for x in self.__movie_list if x.get_movie_name() == movie_name), None)
        if target_moive is None:
            target_moive = Movie(movie_name)
            self.__movie_list.append(target_moive)
        
        movie_actors = target_moive.get_actors()
        for actor in actors:
            # find whether actor name exist in actor list
            target_actor = next((x for x in self.__actor_list if x.get_actor_name() == actor), None)
            if target_actor is None:
                target_actor = Actor(actor)
                self.__actor_list.append(target_actor)

            # add the new movie to target_actor
            new_movie_list = target_actor.get_movies()
            new_movie_list.append(target_moive)
            target_actor.set_movies(new_movie_list)
            
            # add the new actor to target_moive pending list
            movie_actors.append(target_actor)

        target_moive.set_actors(movie_actors)
  
    # we can combine add_rating and updating rating, because they shared the same logic
    def add_and_update_rating(self, name, rating):
        for movie in self.__movie_list:
            if movie.get_movie_name() == name:
                movie.set_rating(rating)

    def get_best_actor(self):
        best_actor = None
        best_rating = 0
        for actor in self.__actor_list:
            current_rating = 0
            movies = actor.get_movies()
            valid_num_movie = 0
            for movie in movies:
                rating = movie.get_rating()
                if rating is not None:
                    current_rating += movie.get_rating()
                    valid_num_movie += 1
            if valid_num_movie > 0:
                current_rating = current_rating/valid_num_movie

            if best_rating < current_rating:
                best_actor = actor
                best_rating = current_rating
        return best_actor

    def get_best_movie(self):
        best_moive = None
        best_rating = 0
        for movie in self.__movie_list:
            rating = movie.get_rating()
            if rating is not None and best_rating < rating:
                best_moive = movie
                best_rating = rating
        return best_moive

# read text line by line
lines =[]
with open("Week3 Collections and Object Oriented Design/movies.txt") as filepath:
    lines = filepath.readlines()

movie_database = MovieDatabase()
for line in lines:
    content = line.replace("\n", "").split(",")
    actor_movie_list = []
    for i in range(1, len(content)):
        actor_name=content[0].strip()
        movie_database.add_movie(content[i].strip(), [actor_name])

with open("Week3 Collections and Object Oriented Design/ratings.txt") as filepath:
    lines = filepath.readlines()
lines = lines[1:]
for line in lines:
    content = line.replace("\n", "").split("\t")
    movie_database.add_and_update_rating(content[0].strip(),int(content[1].strip()))

best_movie = movie_database.get_best_movie()
print(best_movie.get_movie_name(), best_movie.get_rating())

best_actor = movie_database.get_best_actor()
print(best_actor.get_actor_name())