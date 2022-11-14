from Mapper.dataToObject import dataToObject
from MySql.queries import Queries
from observer import Observer

class dishAPI():
    
    __obj = dataToObject()
    __observer1 = Observer(__obj)
    __dishDataObj = __obj.dishObjects()
    __obj.notify_observers("Dish Objects Fetched")
    __nutritionDataObj = __obj.nutritionObjects() 
    __obj.notify_observers("Nutrition Objects Fetched")
    # __obj.unsubscribe(__observer1)

    def getDishes(self):
        formattedData = []
        for i in range(len(self.__dishDataObj)):
            for j in range(len(self.__nutritionDataObj)):
                if self.__dishDataObj[i].getId() == self.__nutritionDataObj[j].getdishId():
                    formattedData.append({"id": self.__dishDataObj[i].getId(), "title": self.__dishDataObj[i].getTitle(), "getreadyInMinutes": self.__dishDataObj[i].getreadyInMinutes(), "getServings": self.__dishDataObj[i].getServings(
                    ), "imageUrl": self.__dishDataObj[i].getImage(), "getCuisines": self.__dishDataObj[i].getCuisines(), "getdishTypes": self.__dishDataObj[i].getdishTypes(), "Instructions": self.__dishDataObj[i].getInstructions(), "getVegetarian": self.__nutritionDataObj[j].getVegetarian(), "getVegan": self.__nutritionDataObj[j].getVegan(), "getGlutenFree": self.__nutritionDataObj[j].getGlutenFree(), "getdairyFree": self.__nutritionDataObj[j].getdairyFree(), "getveryHealthy": self.__nutritionDataObj[j].getveryHealthy(), "getCheap": self.__nutritionDataObj[j].getCheap(), "getveryPopular": self.__nutritionDataObj[j].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
    
    def getNewDishes(self):
        
        self.__obj.getNewReceipes()
        
        # print("get new dishes")
        # queryObj = Queries()
        # observer1 = Observer(queryObj)
        # self.obj.receipesDeleteAllObject()
        dishDataObj = self.__obj.dishObjectsUpdate()
        nutritionDataObj = self.__obj.nutritionObjectsUpdate()
        formattedData = []
        for i in range(len(dishDataObj)):
            for j in range(len(nutritionDataObj)):
                if dishDataObj[i].getId() == nutritionDataObj[j].getdishId():
                    formattedData.append({"id": dishDataObj[i].getId(), "title": dishDataObj[i].getTitle(), "getreadyInMinutes": dishDataObj[i].getreadyInMinutes(), "getServings": dishDataObj[i].getServings(
                    ), "imageUrl": dishDataObj[i].getImage(), "getCuisines": dishDataObj[i].getCuisines(), "getdishTypes": dishDataObj[i].getdishTypes(), "Instructions": dishDataObj[i].getInstructions(), "getVegetarian": nutritionDataObj[j].getVegetarian(), "getVegan": nutritionDataObj[j].getVegan(), "getGlutenFree": nutritionDataObj[j].getGlutenFree(), "getdairyFree": nutritionDataObj[j].getdairyFree(), "getveryHealthy": nutritionDataObj[j].getveryHealthy(), "getCheap": nutritionDataObj[j].getCheap(), "getveryPopular": nutritionDataObj[j].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
