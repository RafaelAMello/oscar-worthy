import os
from neomodel import config

config.DATABASE_URL = os.getenv('NEO4j_DATABASE_URL','bolt://neo4j:password@localhost:7687')
SECRET_KEY = os.getenv('FLASK_SECRET_KEY','A0Zr98j/3yX R~XHH!jmN]LWX/,?RT')
REDIS_URL = os.getenv('REDIS_URL','redis://redis:6379/0')