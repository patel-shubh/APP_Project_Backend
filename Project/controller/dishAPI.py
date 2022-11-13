from Mapper.dataToObject import dataToObject
from MySql.queries import Queries

class dishAPI:
    
    obj = dataToObject()
    dishDataObj = obj.dishObjects()
    nutritionDataObj = obj.nutritionObjects() 

    def getDishes(self):
        formattedData = []
        for i in range(len(self.dishDataObj)):
            for j in range(len(self.nutritionDataObj)):
                if self.dishDataObj[i].getId() == self.nutritionDataObj[j].getdishId():
                    formattedData.append({"id": self.dishDataObj[i].getId(), "title": self.dishDataObj[i].getTitle(), "getreadyInMinutes": self.dishDataObj[i].getreadyInMinutes(), "getServings": self.dishDataObj[i].getServings(
                    ), "imageUrl": self.dishDataObj[i].getImage(), "getCuisines": self.dishDataObj[i].getCuisines(), "getdishTypes": self.dishDataObj[i].getdishTypes(), "Instructions": self.dishDataObj[i].getInstructions(), "getVegetarian": self.nutritionDataObj[j].getVegetarian(), "getVegan": self.nutritionDataObj[j].getVegan(), "getGlutenFree": self.nutritionDataObj[j].getGlutenFree(), "getdairyFree": self.nutritionDataObj[j].getdairyFree(), "getveryHealthy": self.nutritionDataObj[j].getveryHealthy(), "getCheap": self.nutritionDataObj[j].getCheap(), "getveryPopular": self.nutritionDataObj[j].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
    
    def getNewDishes(self):
        
        self.obj.getNewReceipes()
        
        print("get new dishes")
        queryObj = Queries()
        # self.obj.receipesDeleteAllObject()
        dishDataObj = self.obj.dishObjectsUpdate()
        nutritionDataObj = self.obj.nutritionObjectsUpdate()
        formattedData = []
        for i in range(len(dishDataObj)):
            for j in range(len(nutritionDataObj)):
                if dishDataObj[i].getId() == nutritionDataObj[j].getdishId():
                    formattedData.append({"id": dishDataObj[i].getId(), "title": dishDataObj[i].getTitle(), "getreadyInMinutes": dishDataObj[i].getreadyInMinutes(), "getServings": dishDataObj[i].getServings(
                    ), "imageUrl": dishDataObj[i].getImage(), "getCuisines": dishDataObj[i].getCuisines(), "getdishTypes": dishDataObj[i].getdishTypes(), "Instructions": dishDataObj[i].getInstructions(), "getVegetarian": nutritionDataObj[j].getVegetarian(), "getVegan": nutritionDataObj[j].getVegan(), "getGlutenFree": nutritionDataObj[j].getGlutenFree(), "getdairyFree": nutritionDataObj[j].getdairyFree(), "getveryHealthy": nutritionDataObj[j].getveryHealthy(), "getCheap": nutritionDataObj[j].getCheap(), "getveryPopular": nutritionDataObj[j].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
