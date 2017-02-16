from providers.providers import Providers
from threading import Thread

from services.core import Core


class App(object):

    def __init__(self):
        service = Providers.config().launch_service
        print(service)
        if service == "core":
            srv_thread = Thread(target=Core.start, args=(123,))
            srv_thread.setDaemon(True)
            srv_thread.start()
            # Ждем окончания
            srv_thread.join()
        elif service == "api":
            pass

    @staticmethod
    def start():
        App()
