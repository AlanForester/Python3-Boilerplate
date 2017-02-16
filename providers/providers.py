from providers import config, redis, mongo, postgres


class Providers(object):
    @staticmethod
    def mongodb():
        return mongo.get_mongodb()

    @staticmethod
    def postgres():
        return postgres.get_postgres()

    @staticmethod
    def redis():
        return redis.get_redis()

    @staticmethod
    def config():
        return config.get_config()
