from neomodel import StructuredRel
from neomodel import IntegerProperty, StringProperty, StructuredRel

class ActsIn(StructuredRel):
    character   = StringProperty()
    credit_id   = StringProperty()
    order       = IntegerProperty()
    cast_id     = IntegerProperty()
    
class CrewIn(StructuredRel):
    department  = StringProperty()
    credit_id   = StringProperty()
    job         = StringProperty()
