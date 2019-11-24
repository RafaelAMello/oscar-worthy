
from neomodel import StructuredNode
from neomodel import RelationshipFrom
from neomodel import IntegerProperty, StringProperty

class Genre(StructuredNode):
    name        = StringProperty()
    genre_id    = IntegerProperty()
    
    movie_with  = RelationshipFrom('Movie', "IS_KIND")
