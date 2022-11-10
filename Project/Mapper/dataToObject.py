from commonFunction.fetch_api_data import *
from Classes.dishClass import *
from Classes.nutritionClass import *
class dataToObject:
    recipes  = fetchApiData()
    dish = []
    nutrition = []
    
    def dishObjects(self):
        for item in self.recipes:
            self.dish.append(Dish(item['id'],item['title'],str(item['readyInMinutes']),item['servings'],item['image'],str(item['cuisines'],),str(item['dishTypes']),item['instructions']))
        return self.dish
    
    def nutritionObjects(self):
        for item in self.recipes:
            self.nutrition.append(Nutrition(item['id'],item['vegetarian'],item['vegan'],item['glutenFree'],item['dairyFree'],item['veryHealthy'],item['cheap'],item['veryPopular']))
        return self.nutrition
    
    