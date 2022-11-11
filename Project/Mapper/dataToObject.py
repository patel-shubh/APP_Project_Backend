from commonFunction.fetch_api_data import *
from Classes.dishClass import *
from Classes.nutritionClass import *
from Classes.userClass import *
from MySql.queries import *
class dataToObject:
    __recipes  = fetchApiData()
    __userData = fetchUserData()
    __dish = [] 
    __nutrition = []
    __user = []



    def getNewReceipes(self):
        self.__recipes = fetchApiData()
    
    def dishObjects(self):
        for item in self.__recipes:
            self.__dish.append(Dish(item['id'],item['title'],str(item['readyInMinutes']),item['servings'],item['image'] if ('image' in item) else "",str(item['cuisines'],),str(item['dishTypes']),item['instructions']))
        return self.__dish
    
    def nutritionObjects(self):
        for item in self.__recipes:
            self.__nutrition.append(Nutrition(item['id'],item['vegetarian'],item['vegan'],item['glutenFree'],item['dairyFree'],item['veryHealthy'],item['cheap'],item['veryPopular']))
        return self.__nutrition
    
    def userAddObject(self,id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular):
        self.__user.append(User(id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular))
        obj = Queries()
        obj.userInsertOneQuery(self.__user[len(self.__user)-1])
        # return self.__user
    
    def userDeleteObject(self,id):
        index = None
        for i in range(len(self.__user)):
            if self.__user[i].getId()==id:
                index = i
                break
        if index==None:
            print("index none")
        else:
            del self.__user[index]
        obj = Queries()
        obj.userDeleteOneQuery(id)


    def userDeleteAllObject(self):
        self.__dish.clear()
        self.__nutrition.clear()

        
        # return self.__user
    
    def userObjects(self):
        for item in self.__userData:
            # print(item[0])
            self.__user.append(User(item[0],item[1],item[2],item[7],item[3],item[4],item[5],item[6],item[8],item[9],item[10],item[11],item[12],item[13],item[14]))
        return self.__user
    
