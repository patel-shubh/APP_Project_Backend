from Mapper.dataToObject import dataToObject
from MySql.queries import Queries

class dishAPI:
    
    def getDishes(self):
        obj = dataToObject()
        dishDataObj = obj.dishObjects()
        nutritionDataObj = obj.nutritionObjects()   
        formattedData = []
        for i in range(len(dishDataObj)):
            for j in range(len(nutritionDataObj)):
                if dishDataObj[i].getId() == nutritionDataObj[j].getdishId():
                    formattedData.append({"id": dishDataObj[i].getId(), "title": dishDataObj[i].getTitle(), "getreadyInMinutes": dishDataObj[i].getreadyInMinutes(), "imageUrl": dishDataObj[i].getImage(), "getCuisines": dishDataObj[i].getCuisines(), "getdishTypes": dishDataObj[i].getdishTypes(), "Instructions": dishDataObj[i].getInstructions(), "getServings": dishDataObj[i].getServings(
                    ), "getVegetarian": nutritionDataObj[j].getVegetarian(), "getVegan": nutritionDataObj[j].getVegan(), "getGlutenFree": nutritionDataObj[j].getGlutenFree(), "getdairyFree": nutritionDataObj[j].getdairyFree(), "getveryHealthy": nutritionDataObj[j].getveryHealthy(), "getCheap": nutritionDataObj[j].getCheap(), "getveryPopular": nutritionDataObj[j].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
    
    def getNewDishes(self):
        obj = dataToObject()
        obj.getNewReceipes()
        print("get new dishes")
        queryObj = Queries()
        obj.userDeleteAllObject()
        queryObj.dishTableCreator()
        queryObj.nutritionTableCreation()
        dishDataObj = obj.dishObjects()
        nutritionDataObj = obj.nutritionObjects()
        for i in range(len(dishDataObj)):
            queryObj.dishInsertOneQuery(dishDataObj[i])
        for i in range(len(nutritionDataObj)):
            queryObj.nutritionInsertOneQuery(nutritionDataObj[i])
        formattedData = []
        for i in range(len(dishDataObj)):
            for j in range(len(nutritionDataObj)):
                if dishDataObj[i].getId() == nutritionDataObj[j].getdishId():
                    formattedData.append({"id": dishDataObj[i].getId(), "title": dishDataObj[i].getTitle(), "getreadyInMinutes": dishDataObj[i].getreadyInMinutes(), "imageUrl": dishDataObj[i].getImage(), "getCuisines": dishDataObj[i].getCuisines(), "getdishTypes": dishDataObj[i].getdishTypes(), "Instructions": dishDataObj[i].getInstructions(), "getServings": dishDataObj[i].getServings(
                    ), "getVegetarian": nutritionDataObj[j].getVegetarian(), "getVegan": nutritionDataObj[j].getVegan(), "getGlutenFree": nutritionDataObj[j].getGlutenFree(), "getdairyFree": nutritionDataObj[j].getdairyFree(), "getveryHealthy": nutritionDataObj[j].getveryHealthy(), "getCheap": nutritionDataObj[j].getCheap(), "getveryPopular": nutritionDataObj[j].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
