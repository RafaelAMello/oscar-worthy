
from neomodel import StructuredNode
from neomodel import RelationshipFrom
from neomodel import IntegerProperty, StringProperty

class Genre(StructuredNode):
    name        = StringProperty()
    genre_id    = IntegerProperty(unique_index=True)
    movies      = RelationshipFrom('.movie.Movie', "IS_KIND")
