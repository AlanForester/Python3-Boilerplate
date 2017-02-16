from providers.providers import Providers


class Core:
    def __init__(self, param):
        mongo_cur = Providers.mongodb().get_cursor()
        print(mongo_cur, param)

    @staticmethod
    def start(param):
        return Core(param)
