import redis
from datetime import timedelta

def add_to_cache(client: redis.Redis, key: str, value: str, expire_weeks: int = 1):
    with client.pipeline() as pipe:
        pipe.multi()
        pipe.set(key, value)
        pipe.expire(key, int(timedelta(weeks=expire_weeks).total_seconds()))
        pipe.execute()