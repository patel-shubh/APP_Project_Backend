from commonFunction.fetch_api_data import *
from Classes.dishClass import *
from Classes.nutritionClass import *
from Classes.userClass import *
from MySql.queries import *
class dataToObject:
    recipes  = fetchApiData()
    userData = fetchUserData()
    dish = [] # By default, python provides private variable
    nutrition = []
    user = []
    
    def dishObjects(self):
        for item in self.recipes:
            self.dish.append(Dish(item['id'],item['title'],str(item['readyInMinutes']),item['servings'],item['image'],str(item['cuisines'],),str(item['dishTypes']),item['instructions']))
        return self.dish
    
    def nutritionObjects(self):
        for item in self.recipes:
            self.nutrition.append(Nutrition(item['id'],item['vegetarian'],item['vegan'],item['glutenFree'],item['dairyFree'],item['veryHealthy'],item['cheap'],item['veryPopular']))
        return self.nutrition
    
    def userAddObject(self,id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular):
        self.user.append(User(id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular))
        obj = Queries()
        obj.userInsertOneQuery(self.user[len(self.user)-1])
        # return self.user
    
    def userDeleteObject(self,id):
        index = None
        for i in range(len(self.user)):
            if self.user[i].getId()==id:
                index = i
                break
        obj = Queries()
        obj.userDeleteOneQuery(id)
        del self.user[index]
        
        # return self.user
    
    def userObjects(self):
        for item in self.userData:
            # print(item[0])
            self.user.append(User(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13],item[14]))
        return self.user
    
