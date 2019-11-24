from neomodel import StructuredNode
from neomodel import IntegerProperty, StringProperty
from neomodel import RelationshipFrom, RelationshipTo

from .relationships import ActsIn, CrewIn

class Person(StructuredNode):
    name        = StringProperty()
    person_id   = IntegerProperty()
    gender      = IntegerProperty()
    
    acts_in     = RelationshipTo("Movie", "ACTS_IN", model=ActsIn)
    crew_of     = RelationshipTo("Movie", "CREW_IN", model=CrewIn)
