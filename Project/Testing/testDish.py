import pytest
import json
import sys

sys.path.append('../')
from commonFunction.constants import * 
from controller.dishAPI import *
from controller.userAPI import *
from commonFunction.fetch_api_data import fetchUserData

def test_dishObj():
    obj = dishAPI()
    f = open("apiLatestData.txt", "r")
    # print(f.read())
    temp = json.loads(f.read())['recipes']
    # print(temp['recipes'])
    finalData = []
    print(obj.getDishes()['data'])
    for i in range(len(temp)):
        # print(temp[i]['id'])
        finalData.append({"id": temp[i]['id'], "title": temp[i]['title'], "getreadyInMinutes": str(temp[i]['readyInMinutes']), "getServings": str(temp[i]['servings']), "imageUrl": temp[i]['image'], "getCuisines": str(temp[i]['cuisines']), "getdishTypes": str(temp[i]['dishTypes']), "Instructions": temp[i]['instructions'], "getVegetarian": temp[i]['vegetarian'], "getVegan": temp[i]['vegan'], "getGlutenFree": temp[i]['glutenFree'], "getdairyFree": temp[i]['dairyFree'], "getveryHealthy": temp[i]['veryHealthy'], "getCheap": temp[i]['cheap'], "getveryPopular": temp[i]['veryPopular']})
    print("-------------------------------------")
    print(finalData)
    assert obj.getDishes()['data'] == finalData

def test_userObj():
    obj = userAPI()
    temp = fetchUserData()
    print(temp)
    finalData = []
    for i in range(len(temp)):
        print(temp[i][0])
        finalData.append({"id": temp[i][0], "title": temp[i][1], "getreadyInMinutes": temp[i][2], "getServings": temp[i][3], "imageUrl": temp[i][4], "getCuisines": str(temp[i][5]), "getdishTypes": str(temp[i][6]), "Instructions": temp[i][7], "getVegetarian": temp[i][8], "getVegan": temp[i][9], "getGlutenFree": temp[i][10], "getdairyFree": temp[i][11], "getveryHealthy": temp[i][12], "getCheap": temp[i][13], "getveryPopular": temp[i][14]})
    print("-------------------------------------")
    print(finalData)
    assert obj.getUserDish()['data'] == finalData

# test_userObj()