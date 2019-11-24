from datetime import datetime
import pandas as pd
import numpy as np

from app.models import Movie

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
        if np.isnan(value):
            return default_value
        else:
            return datetime.strptime(value, '%Y-%m-%d').date()

    def movie_data(self):
        movie_data_list = []
        for row_n, movie_data in self.df.iterrows():
            n = row_n + 1
            movie_data['release_date']  = self.transform_date(movie_data['release_date'])
            movie_data['revenue']       = self.check_nan(movie_data['revenue'])
            movie_data['vote_count']    = self.check_nan(movie_data['vote_count'])
            movie_data['budget']        = self.check_data_type(movie_data['budget'], int)
            movie_data['popularity']    = self.check_data_type(movie_data['budget'], float)
            movie_data_list.append(movie_data[self.DICT_LIST].to_dict())
            if (n / 100) == (n // 100) or (n == len(self.df)):
                print(f"loading data {n}, {len(movie_data_list)}")
                yield movie_data_list
                movie_data_list = []

        return movie_data_list

def get_data():
    df = pd.read_csv('./data/movies_metadata.csv')
    return df

class SeedMovies:
    def __init__(self):
        self.df = get_data()

    def create_movies(self):
        for movie_list in MovieCSVSerializer().movie_data():
            Movie.create_or_update(*movie_list)
