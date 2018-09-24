import pandas as pd
import numpy as np
from textblob import classifiers
from app.models import Movie

def comedy_classifier():
    movies = Movie.nodes.all()
    df = pd.DataFrame(movies)
    df.columns = ['movies']
    df['is_comedy'] = df['movies'].apply(lambda x:  x.contains_genre.get_or_none(name='Comedy') is not None)
    df['overview'] = df['movies'].apply(lambda x: x.overview)

    all_data = [tuple(x) for x in df[['overview','is_comedy']].values]
    clas = classifiers.NaiveBayesClassifier(all_data)
