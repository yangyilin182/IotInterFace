import redis

class RedisUtil:
    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def hset(self,name,key,value):
        self.r.hset(name,key,value)

    def hget(self):
        pass