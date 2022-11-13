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

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(dataToObject, cls).__new__(cls)
        return cls.instance


    def getNewReceipes(self):
        self.__recipes = fetchApiData()
        print("fetch new data")
    
    def dishObjects(self):
        obj = Queries()
        obj.dishTableCreator()
        print("table data clear")
        for item in self.__recipes:
            self.__dish.append(Dish(item['id'],item['title'],str(item['readyInMinutes']),str(item['servings']),item['image'] if ('image' in item) else "",str(item['cuisines'],),str(item['dishTypes']),item['instructions']))
            obj.dishInsertOneQuery(self.__dish[len(self.__dish)-1])
        return self.__dish
    
    def nutritionObjects(self):
        obj = Queries()
        obj.nutritionTableCreation()
        for item in self.__recipes:
            self.__nutrition.append(Nutrition(item['id'],item['vegetarian'],item['vegan'],item['glutenFree'],item['dairyFree'],item['veryHealthy'],item['cheap'],item['veryPopular']))
            obj.nutritionInsertOneQuery(self.__nutrition[len(self.__nutrition)-1])
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


    def receipesDeleteAllObject(self):
        self.__dish.clear()
        self.__nutrition.clear()
        print("delete objects")

        
        # return self.__user
    
    def userObjects(self):
        self.__userData = fetchUserData()
        self.__user.clear()
        
        for item in self.__userData:
            # print(item[7])
            self.__user.append(User(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13],item[14]))
        return self.__user
    
