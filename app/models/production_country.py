
from neomodel import StructuredNode
from neomodel import RelationshipFrom
from neomodel import StringProperty


class ProductionCountry(StructuredNode):
    iso_3166_1  = StringProperty(unique_index=True)
    name        = StringProperty()
    
    produced    = RelationshipFrom(".movie.Movie", "PRODUCED_IN")
