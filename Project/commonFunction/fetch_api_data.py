import requests
import json
from commonFunction.constants import *
from Connection.connection import Connection
from commonFunction.constants import *

connectionObject = Connection()
cn = connectionObject.conn()
cursor = cn.cursor()

def fetchApiData():
    # callApi = requests.get(API_URL)
    # API_DATA = callApi
    # data = json.loads(callApi.content.decode('utf-8'))
    data = json.loads(API_DATA.decode('utf-8'))
    # print(data['recipes'])
    return data['recipes']

def fetchUserData():
    cursor.execute("select * from user")
    data = cursor.fetchall()
    # print(data)
    return data

    
    



