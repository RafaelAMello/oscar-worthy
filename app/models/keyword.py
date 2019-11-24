
from neomodel import StructuredNode
from neomodel import RelationshipFrom
from neomodel import IntegerProperty, StringProperty

class Keyword(StructuredNode):
    keyword_id      = IntegerProperty()
    name            = StringProperty()
    
    movie_with      = RelationshipFrom("Movie", "CONATINS")
