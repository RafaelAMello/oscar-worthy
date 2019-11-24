
from neomodel import StructuredNode
from neomodel import RelationshipTo
from neomodel import StringProperty

class Language(StructuredNode):
    iso_639_1   = StringProperty()
    name        = StringProperty()
    
    spoken_in   = RelationshipTo("Movie", "SPOKEN_IN")
