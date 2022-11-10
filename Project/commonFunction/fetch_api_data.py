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
    data = json.loads(API_DATA.decode('utf-8'))
    # print(data['recipes'])
    return data['recipes']

def fetchUserData():
    cursor.execute("select * from dish")
    data = cursor.fetchall()
    print(data)
    return data['recipes']

    
    



