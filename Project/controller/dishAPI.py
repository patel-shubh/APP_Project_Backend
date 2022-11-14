from Mapper.dataToObject import dataToObject
from MySql.queries import Queries
from observer import Observer

class dishAPI():
    
    __obj = dataToObject()
    __observer1 = Observer(__obj)
    # __dishDataObj = __obj.dishObjects()
    # __obj.notify_observers("Dish Objects Fetched")
    __recipesDataObj = __obj.recipesObjects() 
    __obj.notify_observers("recipes Objects Fetched")
    # __obj.unsubscribe(__observer1)

    def getDishes(self):
        formattedData = []
        for i in range(len(self.__recipesDataObj)):
            # for j in range(len(self.__recipesDataObj)):
            #     if self.__dishDataObj[i].getId() == self.__recipesDataObj[j].getdishId():
            formattedData.append({"id": self.__recipesDataObj[i].getId(), "title": self.__recipesDataObj[i].getTitle(), "getreadyInMinutes": self.__recipesDataObj[i].getreadyInMinutes(), "getServings": self.__recipesDataObj[i].getServings(
            ), "imageUrl": self.__recipesDataObj[i].getImage(), "getCuisines": self.__recipesDataObj[i].getCuisines(), "getdishTypes": self.__recipesDataObj[i].getdishTypes(), "Instructions": self.__recipesDataObj[i].getInstructions(), "getVegetarian": self.__recipesDataObj[i].getVegetarian(), "getVegan": self.__recipesDataObj[i].getVegan(), "getGlutenFree": self.__recipesDataObj[i].getGlutenFree(), "getdairyFree": self.__recipesDataObj[i].getdairyFree(), "getveryHealthy": self.__recipesDataObj[i].getveryHealthy(), "getCheap": self.__recipesDataObj[i].getCheap(), "getveryPopular": self.__recipesDataObj[i].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
    
    def getNewDishes(self):
        
        self.__obj.getNewReceipes()
        
        # print("get new dishes")
        # queryObj = Queries()
        # observer1 = Observer(queryObj)
        # self.obj.receipesDeleteAllObject()
        # dishDataObj = self.__obj.dishObjectsUpdate()
        recipesDataObj = self.__obj.recipesObjectsUpdate()
        formattedData = []
        for i in range(len(recipesDataObj)):
                
            formattedData.append({"id": recipesDataObj[i].getId(), "title": recipesDataObj[i].getTitle(), "getreadyInMinutes": recipesDataObj[i].getreadyInMinutes(), "getServings": recipesDataObj[i].getServings(
            ), "imageUrl": recipesDataObj[i].getImage(), "getCuisines": recipesDataObj[i].getCuisines(), "getdishTypes": recipesDataObj[i].getdishTypes(), "Instructions": recipesDataObj[i].getInstructions(), "getVegetarian": recipesDataObj[i].getVegetarian(), "getVegan": recipesDataObj[i].getVegan(), "getGlutenFree": recipesDataObj[i].getGlutenFree(), "getdairyFree": recipesDataObj[i].getdairyFree(), "getveryHealthy": recipesDataObj[i].getveryHealthy(), "getCheap": recipesDataObj[i].getCheap(), "getveryPopular": recipesDataObj[i].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
