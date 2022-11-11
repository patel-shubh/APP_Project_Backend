from Mapper.dataToObject import dataToObject


class dishAPI:
    formattedData = []
    obj = dataToObject()
    dishDataObj = obj.dishObjects()
    nutritionDataObj = obj.nutritionObjects()

    def getDishes(self):
        for i in range(len(self.dishDataObj)):
            for j in range(len(self.nutritionDataObj)):
                if self.dishDataObj[i].getId() == self.nutritionDataObj[j].getdishId():
                    self.formattedData.append({"id": self.dishDataObj[i].getId(), "title": self.dishDataObj[i].getTitle(), "getreadyInMinutes": self.dishDataObj[i].getreadyInMinutes(), "imageUrl": self.dishDataObj[i].getImage(), "getCuisines": self.dishDataObj[i].getCuisines(), "getdishTypes": self.dishDataObj[i].getdishTypes(), "Instructions": self.dishDataObj[i].getInstructions(), "getServings": self.dishDataObj[i].getServings(
                    ), "getVegetarian": self.nutritionDataObj[j].getVegetarian(), "getVegan": self.nutritionDataObj[j].getVegan(), "getGlutenFree": self.nutritionDataObj[j].getGlutenFree(), "getdairyFree": self.nutritionDataObj[j].getdairyFree(), "getveryHealthy": self.nutritionDataObj[j].getveryHealthy(), "getCheap": self.nutritionDataObj[j].getCheap(), "getveryPopular": self.nutritionDataObj[j].getveryPopular()})

        return {"success": "true",
                "status": 200,
                "data": self.formattedData}
