from neomodel import StructuredNode
from neomodel import IntegerProperty, StringProperty, DateProperty, FloatProperty
from neomodel import RelationshipFrom, RelationshipTo

from .relationships import ActsIn, CrewIn

class Movie(StructuredNode):
    movie_id            = IntegerProperty()
    homepage            = StringProperty()
    original_language   = StringProperty()
    original_title      = StringProperty()
    overview            = StringProperty()
    popularity          = FloatProperty()
    release_date        = DateProperty()
    revenue             = IntegerProperty()
    runtime             = FloatProperty()
    tagline             = StringProperty()
    title               = StringProperty()
    vote_average        = FloatProperty()
    vote_count          = IntegerProperty()

    contains_genre      = RelationshipTo("Genre", "IS_KIND")
    contains_language   = RelationshipFrom('Language', "SPOKEN_IN")
    contains_keyword    = RelationshipTo("Keyword", "CONTAINS")
    produced_by         = RelationshipFrom("ProductionCompany", "PRODUCED_BY")
    produced_in         = RelationshipTo("ProductionCountry", "PRODUCED_IN")
    acted_in            = RelationshipFrom("Person", "ACTS_IN", model=ActsIn)
    crew_in             = RelationshipFrom("Person", "CREW_IN", model=CrewIn)
