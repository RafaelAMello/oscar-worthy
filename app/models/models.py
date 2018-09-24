from neomodel import StructuredNode, IntegerProperty, StringProperty, DateProperty, \
FloatProperty, RelationshipFrom, RelationshipTo, StructuredRel

class ActsIn(StructuredRel):
    character = StringProperty()
    credit_id = StringProperty()
    order = IntegerProperty()
    cast_id = IntegerProperty()
    
class CrewIn(StructuredRel):
    department = StringProperty()
    credit_id = StringProperty()
    job = StringProperty()
    
class Movie(StructuredNode):
    movie_id = IntegerProperty()
    homepage = StringProperty()
    original_language = StringProperty()
    original_title = StringProperty()
    overview = StringProperty()
    popularity = FloatProperty()
    release_date = DateProperty()
    revenue = IntegerProperty()
    runtime = FloatProperty()
    tagline = StringProperty()
    title = StringProperty()
    vote_average = FloatProperty()
    vote_count = IntegerProperty()

    contains_genre = RelationshipTo("Genre", "IS_KIND")
    contains_language = RelationshipFrom('Language', "SPOKEN_IN")
    contains_keyword = RelationshipTo("Keyword", "CONTAINS")
    produced_by = RelationshipFrom("ProductionCompany", "PRODUCED_BY")
    produced_in = RelationshipTo("ProductionCountry", "PRODUCED_IN")
    
    acted_in = RelationshipFrom("Person", "ACTS_IN", model=ActsIn)
    crew_in = RelationshipFrom("Person", "CREW_IN", model=CrewIn)
    
class Genre(StructuredNode):
    name = StringProperty()
    genre_id = IntegerProperty()
    
    movie_with = RelationshipFrom('Movie', "IS_KIND")
    
class Keyword(StructuredNode):
    keyword_id = IntegerProperty()
    name = StringProperty()
    
    movie_with = RelationshipFrom("Movie", "CONATINS")
    
class ProductionCompany(StructuredNode):
    company_id = IntegerProperty()
    name = StringProperty()
    
    produced = RelationshipTo("Movie", "PRODUCED_BY")
    
class ProductionCountry(StructuredNode):
    iso_3166_1 = StringProperty()
    name = StringProperty()
    
    produced = RelationshipFrom("Movie", "PRODUCED_IN")
    
class Language(StructuredNode):
    iso_639_1 = StringProperty()
    name = StringProperty
    
    spoken_in = RelationshipTo("Movie", "SPOKEN_IN")
    
class Person(StructuredNode):
    name = StringProperty()
    person_id = IntegerProperty()
    gender = IntegerProperty()
    
    acts_in = RelationshipTo("Movie", "ACTS_IN", model=ActsIn)
    crew_of = RelationshipTo("Movie", "CREW_IN", model=CrewIn)