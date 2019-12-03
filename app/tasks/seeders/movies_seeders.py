from datetime import datetime
import pandas as pd
import numpy as np
from tqdm import tqdm
import multiprocessing as mp

from app.models import Movie, Genre, ProductionCompany

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

    def __init__(self, df):
        self.df = df
        self.df['oid'] = self.df['id']

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

    def process_production_companies_data(self, raw_production_companies_string):
        production_companies_list = []
        raw_production_companies_list = eval(raw_production_companies_string)
        for raw_production_company in raw_production_companies_list:
            production_companies_list.append({
                'company_id' : raw_production_company['id'],
                'name'       : raw_production_company['name']
            })
        return production_companies_list

    def __call__(self):
        movie_data_list = []
        genre_data_list = []
        production_companies_list = []
        for row_n, movie_data in self.df.iterrows():
            movie_data_list.append(self.process_movie_data(movie_data))
            genre_data_list.append(self.process_genre_data(movie_data['genres']))
            production_companies_list.append(self.process_production_companies_data(movie_data['production_companies']))
        self.save_data(movie_data_list, genre_data_list, production_companies_list)

    def save_data(self, movie_data_list, genre_data_list, production_companies_list):
        movie_objects = Movie.get_or_create(*movie_data_list)
        for n, genres in enumerate(genre_data_list):
            movie = movie_objects[n]
            genres_objects = Genre.get_or_create(*genres)
            [movie.genres.connect(genre) for genre in genres_objects]
        for n, production_companies in enumerate(production_companies_list):
            movie = movie_objects[n]
            production_companies_objects = ProductionCompany.get_or_create(*production_companies)
            [movie.produced_by.connect(production_company) for production_company in production_companies_objects]

def get_data():
    return [chunk for chunk in pd.read_csv('./data/movies_metadata.csv', chunksize=100)]

def process_chunksize(df):
    serializer = MovieCSVSerializer(df)
    serializer()

class tracker:
    def __init__(self, df_list):
        self.pbar = tqdm(total=len(df_list))

    def __call__(self, *a):
        self.pbar.update()

def run():
    df_list = get_data()
    t = tracker(df_list)
    pool = mp.Pool(5)

    for df in df_list:
        pool.apply_async(process_chunksize, args=(df,), callback=t)

    pool.close()
    pool.join()

if __name__ == '__main__':
    run()
