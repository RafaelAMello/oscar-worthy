
from neomodel import StructuredNode
from neomodel import RelationshipTo
from neomodel import IntegerProperty, StringProperty


class ProductionCompany(StructuredNode):
    company_id  = IntegerProperty(unique_index=True)
    name        = StringProperty()
    
    produced    = RelationshipTo(".movie.Movie", "PRODUCED_BY")
