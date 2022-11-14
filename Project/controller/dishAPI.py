from Mapper.dataToObject import dataToObject
from observer import Observer


class dishAPI():

    _obj = dataToObject()
    _observer1 = Observer(_obj)
    # _dishDataObj = _obj.dishObjects()
    # _obj.notify_observers("Dish Objects Fetched")
    _recipesDataObj = _obj.recipesObjects()
    _obj.notify_observers("recipes Objects Fetched")
    # _obj.unsubscribe(_observer1)

    def getDishes(self):
        formattedData = []
        for i in range(len(self._recipesDataObj)):
            # for j in range(len(self._recipesDataObj)):
            #     if self._dishDataObj[i].getId() == self._recipesDataObj[j].getdishId():
            formattedData.append({"id": self._recipesDataObj[i].getId(), "title": self._recipesDataObj[i].getTitle(), "getreadyInMinutes": self._recipesDataObj[i].getreadyInMinutes(), "getServings": self._recipesDataObj[i].getServings(
            ), "imageUrl": self._recipesDataObj[i].getImage(), "getCuisines": self._recipesDataObj[i].getCuisines(), "getdishTypes": self._recipesDataObj[i].getdishTypes(), "Instructions": self._recipesDataObj[i].getInstructions(), "getVegetarian": self._recipesDataObj[i].getVegetarian(), "getVegan": self._recipesDataObj[i].getVegan(), "getGlutenFree": self._recipesDataObj[i].getGlutenFree(), "getdairyFree": self._recipesDataObj[i].getdairyFree(), "getveryHealthy": self._recipesDataObj[i].getveryHealthy(), "getCheap": self._recipesDataObj[i].getCheap(), "getveryPopular": self._recipesDataObj[i].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}

    def getNewDishes(self):

        self._obj.getNewReceipes()

        # print("get new dishes")
        # queryObj = Queries()
        # observer1 = Observer(queryObj)
        # self.obj.receipesDeleteAllObject()
        # dishDataObj = self._obj.dishObjectsUpdate()
        recipesDataObj = self._obj.recipesObjectsUpdate()
        formattedData = []
        for i in range(len(recipesDataObj)):

            formattedData.append({"id": recipesDataObj[i].getId(), "title": recipesDataObj[i].getTitle(), "getreadyInMinutes": recipesDataObj[i].getreadyInMinutes(), "getServings": recipesDataObj[i].getServings(
            ), "imageUrl": recipesDataObj[i].getImage(), "getCuisines": recipesDataObj[i].getCuisines(), "getdishTypes": recipesDataObj[i].getdishTypes(), "Instructions": recipesDataObj[i].getInstructions(), "getVegetarian": recipesDataObj[i].getVegetarian(), "getVegan": recipesDataObj[i].getVegan(), "getGlutenFree": recipesDataObj[i].getGlutenFree(), "getdairyFree": recipesDataObj[i].getdairyFree(), "getveryHealthy": recipesDataObj[i].getveryHealthy(), "getCheap": recipesDataObj[i].getCheap(), "getveryPopular": recipesDataObj[i].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": formattedData}
