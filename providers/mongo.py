import providers.globals as gvars

from providers.config import get_config
from pymongo import MongoClient


def get_mongodb():
    if not gvars.APP_MONGODB:
        gvars.APP_MONGODB = MongoDB()
    return gvars.APP_MONGODB


class MongoDB:
    connections_count = 5
    connection_used = 0

    hostname = None
    port = None
    database = None

    _connections = []

    def __init__(self):
        config = get_config()
        self.hostname = config.get_mongodb_hostname()
        self.port = config.get_mongodb_port()
        self.database = config.get_mongodb_db()

        i = 0
        while i < self.connections_count:
            self._connections.append(self.connect())
            i += 1

    def connect(self):
        connection = MongoClient(host=self.hostname+":"+self.port, document_class=dict)
        return connection[self.database]

    def get_cursor(self):
        db = self._connections[self.connection_used]
        if self.connection_used >= len(self._connections) - 1:
            self.connection_used = 0
        return db

