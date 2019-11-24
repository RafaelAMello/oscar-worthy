
from neomodel import StructuredNode
from neomodel import RelationshipTo
from neomodel import IntegerProperty, StringProperty


class ProductionCompany(StructuredNode):
    company_id  = IntegerProperty()
    name        = StringProperty()
    
    produced    = RelationshipTo("Movie", "PRODUCED_BY")
