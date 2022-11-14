import requests
import json
from commonFunction.constants import *
from Connection.connection import Connection
from observer import Observer

class dataFetcher(object):

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    _connectionObject = Connection()
    _observer1 = Observer(_connectionObject)
    _cn = _connectionObject.conn()
    _connectionObject.notify_observers("Connection Established and Returned")
    _cursor = _cn.cursor()

    def fetchApiData(self):
        callApi = requests.get(API_URL)
        data = json.loads(callApi.content.decode('utf-8'))
        
        # f = open("apiLatestData.txt", "w")
        # f.write(callApi.content.decode('utf-8'))
        # f.close()
        # print( "fetch api called",API_DATA)
        # data = json.loads(API_DATA.decode('utf-8'))
        print(data['recipes'])
        with open("../apiLatestData.txt", "w", encoding="utf-8") as f:
            f.write(callApi.content.decode('utf-8'))
        return data['recipes']

    def fetchUserData(self):
        self._cursor.execute("select * from user")
        data = self._cursor.fetchall()
        # print(data)
        return data

    
    



