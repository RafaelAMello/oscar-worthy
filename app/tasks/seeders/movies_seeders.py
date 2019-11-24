from datetime import datetime
import pandas as pd
import numpy as np

from app.models import Movie, Genre

class MovieCSVSerializer:
    DICT_LIST = [
        'oid',
        'imdb_id',
        'original_title',
        'title',
        'original_language',
        'overview',
        'popularity',
        'status',
        'tagline',
        'adult',
        'poster_path',
        'video',
        'release_date',
        'revenue',
        'budget',
        'runtime',
        'homepage',
        'vote_average',
        'vote_count'
    ]

    def __init__(self):
        self.df = get_data()
        self.df['oid'] = self.df['id']
        # data_dict['release_date'] = datetime.strptime(data_dict['release_date'], '%Y-%m-%d')

    def check_nan(self, value, default_value=None):
        if np.isnan(value):
            return default_value
        else:
            return value
    
    def check_data_type(self, value, datatype, default_value=None):
        if value is datatype:
            return value
        else:
            return default_value

    def transform_date(self, value, default_value=None):
        if type(value) == str:
            try:
                return datetime.strptime(value, '%Y-%m-%d').date()
            except ValueError:
                return default_value
        elif np.isnan(value):
            return default_value

    def process_movie_data(self, raw_movie_data):
        raw_movie_data['release_date']  = self.transform_date(raw_movie_data['release_date'])
        raw_movie_data['revenue']       = self.check_nan(raw_movie_data['revenue'])
        raw_movie_data['vote_count']    = self.check_nan(raw_movie_data['vote_count'])
        raw_movie_data['budget']        = self.check_data_type(raw_movie_data['budget'], int)
        raw_movie_data['popularity']    = self.check_data_type(raw_movie_data['budget'], float)
        return raw_movie_data[self.DICT_LIST].to_dict()
    
    def process_genre_data(self, raw_genre_list_string):
        processed_genre_lst = []
        raw_genre_list = eval(raw_genre_list_string)
        for raw_genre in raw_genre_list:
            processed_genre_lst.append({
                'genre_id'  : raw_genre['id'],
                'name'      : raw_genre['name']
            })
        return processed_genre_lst

    def movie_data(self):
        movie_data_list = []
        genre_data_list = []
        for row_n, movie_data in self.df.iterrows():
            n = row_n + 1
            movie_data_list.append(self.process_movie_data(movie_data))
            genre_data_list.append(self.process_genre_data(movie_data['genres']))

            if (n / 100) == (n // 100) or (n == len(self.df)):
                print(f"loading data {n}, {len(movie_data_list)}")
                yield movie_data_list, genre_data_list
                movie_data_list = []
                genre_data_list = []

        return movie_data_list

def get_data():
    df = pd.read_csv('./data/movies_metadata.csv')
    return df

class SeedMovies:
    def __init__(self):
        self.df = get_data()

    def create_movies(self):
        for movie_list, genre_list in MovieCSVSerializer().movie_data():
            movie_objects = Movie.get_or_create(*movie_list)
            for n, genres in enumerate(genre_list):
                movie = movie_objects[n]
                genres_objects = Genre.get_or_create(*genres)
                for genre in genres_objects:
                    movie.genres.connect(genre)
