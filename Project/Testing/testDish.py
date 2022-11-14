import pytest
import json
import sys
from fastapi.testclient import TestClient

sys.path.append('../')
from commonFunction.constants import * 
from controller.dishAPI import *
from controller.userAPI import *
from commonFunction.fetch_api_data import fetchUserData

client = TestClient(app)


def testDishObj():
    obj = dishAPI()
    f = open("../apiLatestData.txt", "r")
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

# API Testing 
def testGetDishAPI():
    res = client.get('/')
    assert res.status_code == STATUS_CODE_FOR_SUCCESS

def testAddUserDishAPI():
    res = client.post('/dish/add/',json={
            "id": 655043,
            "title": "PB Cup Stuffed Brownie Bites",
            "getreadyInMinutes": "45",
            "imageUrl": "https://spoonacular.com/recipeImages/655043-556x370.jpg",
            "getCuisines": "['American']",
            "getdishTypes": "['dessert']",
            "Instructions": "Whisk together sugar, flour, eggs, salt, oil, vanilla, and cocoa powder until well combined. Stir in the semi sweet chocolate chips. Make sure to not over mix!\nPrepare a mini muffin pan with cooking spray and preheat your oven to 350 degrees F.\nScoop batter into the pan.\nFill the slots up about  -  of the way up, so there's a little room for the peanut butter cup stuffed brownie bites to rise.\nCook for 8 - 10 minutes, or until an inserted toothpick comes out almost clean. It's ok if these are slightly underdone.\nOnce the brownies are done, gently push a peanut butter cup in the center of the brownie. Let these set in the pan for a couple of minutes.\nRemove from the pan and let them cool the rest of the way on a cooling rack!",
            "getServings": 60,
            "getVegetarian": "false",
            "getVegan": "false",
            "getGlutenFree": "false",
            "getdairyFree": "true",
            "getveryHealthy": "false",
            "getCheap": "false",
            "getveryPopular": "false"
    })
    assert res.status_code == STATUS_CODE_FOR_SUCCESS

def testRemoveUserDishAPI():
    response = client.post('/dish/remove',json={"id":"655043"})
    assert response.status_code == STATUS_CODE_FOR_SUCCESS   

# def testGetDishAPI():
#     response =  getDish()
#     assert response['status'] == STATUS_CODE_FOR_SUCCESS

# def testUserDishAPI():
#     response = userDish()
#     assert response['status'] == STATUS_CODE_FOR_SUCCESS
    
# def testGetRandomDishAPI():
#     response =refreshDish()
#     assert response['status'] == STATUS_CODE_FOR_SUCCESS

# @pytest.mark.asyncio
# async def testAddUserDishAPI():
#     response = await addUser(Request(DATA_FOR_TESTING))
#     assert response['status'] == STATUS_CODE_FOR_SUCCESS

# @pytest.mark.asyncio
# async def testRemoveUserDishAPI():
#     response = await removeUser(Request(DATA_FOR_TESTING))
#     assert response['status'] == STATUS_CODE_FOR_SUCCESS
