from neomodel import StructuredNode
from neomodel import IntegerProperty, StringProperty, DateProperty, FloatProperty, BooleanProperty
from neomodel import RelationshipFrom, RelationshipTo

from .relationships import ActsIn, CrewIn
from .genre import Genre
from .language import Language
from .keyword import Keyword
from .production_company import ProductionCompany
from .production_country import ProductionCountry
from .person import Person

class Movie(StructuredNode):
    oid                 = StringProperty(unique_index=True)
    imdb_id             = StringProperty()
    original_title      = StringProperty()
    title               = StringProperty()
    original_language   = StringProperty()
    overview            = StringProperty()
    popularity          = FloatProperty()
    status              = StringProperty()
    tagline             = StringProperty()
    adult               = BooleanProperty()
    poster_path         = StringProperty()
    video               = StringProperty()
    release_date        = DateProperty()
    revenue             = IntegerProperty()
    budget              = IntegerProperty()
    runtime             = FloatProperty()
    homepage            = StringProperty()
    vote_average        = FloatProperty()
    vote_count          = IntegerProperty()
    
    genres              = RelationshipTo("Genre", "IS_KIND")
    spoken_languages    = RelationshipFrom("Language", "SPOKEN_IN")
    keywords            = RelationshipTo("Keyword", "CONTAINS")
    produced_by         = RelationshipFrom("ProductionCompany", "PRODUCED_BY")
    produced_in         = RelationshipTo("ProductionCountry", "PRODUCED_IN")

    acted_in            = RelationshipFrom("Person", "ACTS_IN", model=ActsIn)
    crew_in             = RelationshipFrom("Person", "CREW_IN", model=CrewIn)
