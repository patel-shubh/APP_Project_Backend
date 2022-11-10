import mysql.connector as connector

class Connection(object):
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Connection, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
    
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