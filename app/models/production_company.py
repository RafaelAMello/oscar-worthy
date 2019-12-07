
from neomodel import StructuredNode
from neomodel import RelationshipFrom
from neomodel import IntegerProperty, StringProperty


class ProductionCompany(StructuredNode):
    company_id  = IntegerProperty(unique_index=True)
    name        = StringProperty()
    
    produced    = RelationshipFrom(".movie.Movie", "PRODUCED_BY")
