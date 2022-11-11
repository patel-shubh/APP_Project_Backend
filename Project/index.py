
from Mapper.dataToObject import *
from MySql.queries import *
import json
import asyncio
import time
# insertTable()

# fetchApiData()
# fetchUserData()
# a = dishAPI()
# print(a.getDishes())

obj = dataToObject()
dishDataObj = obj.dishObjects()
nutritionDataObj = obj.nutritionObjects()
userDataObj = obj.userObjects()
queryObj = Queries()
queryObj.dishTableCreator()
queryObj.nutritionTableCreation()
queryObj.userTableCreator()
for i in range(len(dishDataObj)):
    queryObj.dishInsertOneQuery(dishDataObj[i])
for i in range(len(nutritionDataObj)):
    queryObj.nutritionInsertOneQuery(nutritionDataObj[i])

