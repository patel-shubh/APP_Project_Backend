from controller.insertTable import *
from Mapper.dataToObject import *
from MySql.queries import *

# insertTable()

# fetchApiData()
# fetchUserData()

obj = dataToObject()
dishDataObj = obj.dishObjects()
nutritionDataObj = obj.nutritionObjects()
userDataObj = obj.userObjects()
obj.userDeleteObject(2)
print(userDataObj)
queryObj = Queries()
queryObj.dishTableCreator()
queryObj.nutritionTableCreation()
queryObj.userTableCreator()
for i in range(len(dishDataObj)):
    queryObj.dishInsertOneQuery(dishDataObj[i])
for i in range(len(nutritionDataObj)):
    queryObj.nutritionInsertOneQuery(nutritionDataObj[i])