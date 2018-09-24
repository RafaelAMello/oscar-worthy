import redis
import rq

from .trainers.genre_comedy import comedy_classifier

def setup_rq(app):
    redis_server = redis.StrictRedis.from_url(app.config['REDIS_URL'])
    queue = rq.Queue(connection=redis_server)
    return queue