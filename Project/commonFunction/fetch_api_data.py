import requests
import json
from commonFunction.constants import *


def fetchApiData():
    # callApi = requests.get(API_URL)
    data = json.loads(API_DATA.decode('utf-8'))
    return data['recipes']

    
    



