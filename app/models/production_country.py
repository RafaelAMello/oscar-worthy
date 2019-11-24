
from neomodel import StructuredNode
from neomodel import RelationshipFrom
from neomodel import StringProperty


class ProductionCountry(StructuredNode):
    iso_3166_1 = StringProperty()
    name       = StringProperty()
    
    produced = RelationshipFrom("Movie", "PRODUCED_IN")
