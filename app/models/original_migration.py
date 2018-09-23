from dateutil import parser
from sys import stdout

from app.models.models import *
from sys import stdout
import pandas as pd

pinfo = parser.parserinfo(yearfirst=True)
date_parser = parser.parser()
date_parser.info = pinfo

df = pd.read_csv('tmdb_5000_movies.csv')
df.index = df['id']
df['genres'] = df['genres'].apply(eval)
df['keywords'] = df['keywords'].apply(eval)
df['production_companies'] = df['production_companies'].apply(eval)
df['production_countries'] = df['production_countries'].apply(eval)
df['spoken_languages'] = df['spoken_languages'].apply(eval)

df2 = pd.read_csv('tmdb_5000_credits.csv')
df2.index = df2['movie_id']
df2.drop('movie_id', axis=1)
df_combined = df.join(df2.drop('title', axis=1))
df_combined['cast'] = df_combined['cast'].apply(eval)
df_combined['crew'] = df_combined['crew'].apply(eval)
df_combined = df_combined[df_combined['status'] == 'Released']


for row in range(len(df_combined)):
    movie_data = df_combined.iloc[row]
    stdout.write("\rWriting {} Completed {}".format(movie_data['title'], round((row/len(df_combined))*100,2)) + 50 * " ")
    stdout.flush()
    movie = Movie(
        movie_id = movie_data['id'],
        homepage = movie_data['homepage'],
        original_language = movie_data['original_language'],
        original_title = movie_data['original_title'],
        overview = movie_data['overview'],
        popularity = movie_data['popularity'],
        release_date = date_parser.parse(movie_data['release_date']).date() if movie_data['release_date'] == movie_data['release_date'] else None,
        revenue = movie_data['revenue'],
        runtime = movie_data['runtime'],
        tagline = movie_data['tagline'],
        title = movie_data['title'],
        vote_average = movie_data['vote_average'],
        vote_count = movie_data['vote_count']
        ).save()

    for genre_data in movie_data['genres']:
        query = Genre.nodes.filter(genre_id=genre_data['id'])
        if not query.all():
            genre = Genre(
                name = genre_data['name'],
                genre_id = genre_data['id']
            ).save()
        else:
            genre = query.all()[0]
        movie.contains_genre.connect(genre)

    for keyword_data in movie_data['keywords']:
        query = Keyword.nodes.filter(keyword_id=keyword_data['id'])
        if not query.all():
            keyword = Keyword(
                name = keyword_data['name'],
                keyword_id = keyword_data['id']
            ).save()
        else:
            keyword = query.all()[0]
        movie.contains_keyword.connect(keyword)

    for production_company_data in movie_data['production_companies']:
        query = ProductionCompany.nodes.filter(company_id=production_company_data['id'])
        if not query.all():
            production_company = ProductionCompany(
                name = production_company_data['name'],
                company_id = production_company_data['id']
            ).save()
        else:
            production_company = query.all()[0]
        movie.produced_by.connect(production_company)
        
    for production_country_data in movie_data['production_countries']:
        query = ProductionCountry.nodes.filter(iso_3166_1=production_country_data['iso_3166_1'])
        if not query.all():
            production_country = ProductionCountry(
                name = production_country_data['name'],
                iso_3166_1 = production_country_data['iso_3166_1']
            ).save()
        else:
            production_country = query.all()[0]
        movie.produced_in.connect(production_country)
        
    for language_data in movie_data['spoken_languages']:
        query = Language.nodes.filter(iso_639_1=language_data['iso_639_1'])
        if not query.all():
            language = Language(
                iso_639_1 = language_data['iso_639_1'],
                name = language_data['name']
            ).save()
        else:
            language = query.all()[0]
        movie.contains_language.connect(language)
        
    for cast_data in movie_data['cast']:
        query = Person.nodes.filter(person_id=cast_data['id'])
        if not query.all():
            person = Person(
                name = cast_data['name'],
                person_id = cast_data['id'],
                gender = cast_data['gender']
            ).save()
        else:
            person = query.all()[0]
        
        acting_relastionship = person.acts_in.connect(movie)
        acting_relastionship.character = cast_data['character']
        acting_relastionship.order = cast_data['order']
        acting_relastionship.cast_id = cast_data['cast_id']
        acting_relastionship.credit_id = cast_data['credit_id']
        acting_relastionship.save()
        
    for cast_data in movie_data['crew']:
        query = Person.nodes.filter(person_id=cast_data['id'])
        if not query.all():
            person = Person(
                name = cast_data['name'],
                person_id = cast_data['id'],
                gender = cast_data['gender']
            ).save()
        else:
            person = query.all()[0]
        
        crew_relastionship = person.crew_of.connect(movie)
        crew_relastionship.department = cast_data['department']
        crew_relastionship.job = cast_data['job']
        crew_relastionship.credit_id = cast_data['credit_id']
        crew_relastionship.save()
        