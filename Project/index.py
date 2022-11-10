from controller.insertTable import *
from Mapper.dataToObject import *
from MySql.queries import *

# insertTable()

obj = dataToObject()
dishDataObj = obj.dishObjects()
nutritionDataObj = obj.nutritionObjects()
queryObj = Queries()
queryObj.dishTableCreator()
queryObj.nutritionTableCreation()

for i in range(len(dishDataObj)):
    queryObj.dishInsertOneQuery(dishDataObj[i])
for i in range(len(nutritionDataObj)):
    queryObj.nutritionInsertOneQuery(nutritionDataObj[i])