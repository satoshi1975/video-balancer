import json
import redis

redis_client = redis.Redis(host='redis', port=6379, db=0)
CACHE_TTL = 60 * 5

def get_cache(key: str):
    cached_data = redis_client.get(key)
    if cached_data:
        return json.loads(cached_data) 
    return None

def set_cache(key: str, data, ttl=CACHE_TTL):
    redis_client.setex(key, ttl, json.dumps(data))