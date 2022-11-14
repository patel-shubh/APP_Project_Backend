import requests
import json
from commonFunction.constants import *
from Connection.connection import Connection


# __connectionObject = Connection()
# __cn = __connectionObject.conn()
# __cursor = __cn.__cursor()

class dataFetcher:
    __connectionObject = Connection()
    __cn = __connectionObject.conn()
    __cursor = __cn.cursor()

    def fetchApiData(self):
        callApi = requests.get(API_URL)
        data = json.loads(callApi.content.decode('utf-8'))
        
        # f = open("apiLatestData.txt", "w")
        # f.write(callApi.content.decode('utf-8'))
        # f.close()
        # print( "fetch api called",API_DATA)
        # data = json.loads(API_DATA.decode('utf-8'))
        # print(data['recipes'])
        with open("../apiLatestData.txt", "w", encoding="utf-8") as f:
            f.write(callApi.content.decode('utf-8'))
        return data['recipes']

    def fetchUserData(self):
        self.__cursor.execute("select * from user")
        data = self.__cursor.fetchall()
        # print(data)
        return data

    
    



