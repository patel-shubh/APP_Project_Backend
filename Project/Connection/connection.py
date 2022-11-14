import mysql.connector as connector

from observer import Observer

class Connection(object):
    # _instance = None

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self._observers.remove(Observer)
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Connection, cls).__new__(cls)
        return cls.instance

    # def __new__(cls):
    #     if cls._instance is None:
    #         print('Creating the object')
    #         cls._instance = super(Connection, cls).__new__(cls)
    #         # Put any initialization here.
    #     return cls._instance
    
    def conn(cls):
        config = {
            "host":"localhost",
            "user":"root",
            "password":"",
            "database": "app_project"
        }
        try:
            c = connector.connect(autocommit = True,**config)
            return c
        except:
            print("connection error")
            exit(1)