
from neomodel import StructuredNode
from neomodel import RelationshipFrom
from neomodel import IntegerProperty, StringProperty


class Collection(StructuredNode):
    collection_id   = IntegerProperty(unique_index=True)
    name            = StringProperty()
    poster_path     = StringProperty()
    backdrop_path   = StringProperty()
    
    has_movies      = RelationshipFrom(".movie.Movie", "IS_PART_OF")
