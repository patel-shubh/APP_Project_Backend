from commonFunction.fetch_api_data import *
from Classes.dishClass import *
from Classes.nutritionClass import *
from Classes.userClass import *
from MySql.queries import *
from observer import Observer

class dataToObject(object):

    __fetcherObj = dataFetcher()
    __observer2 = Observer(__fetcherObj)
    __data  = __fetcherObj.fetchApiData()
    __fetcherObj.notify_observers("Parent API data fetched")
    __userData = __fetcherObj.fetchUserData()
    __recipes = []
    __user = []
    __obj = Queries()
    __observer1 = Observer(__obj)

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        # print("subscriber append",observer)
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

        def __new__(cls):
            if not hasattr(cls, 'instance'):
                cls.instance = super(dataToObject, cls).__new__(cls)
            return cls.instance

    def getNewReceipes(self):
        self.__data = self.__fetcherObj.fetchApiData()
        self.__fetcherObj.notify_observers("Parent API data fetched to get new data")
    
    def recipesObjects(self):
        self.__obj.dishTableCreator()
        self.__obj.nutritionTableCreation()
        self.__obj.notify_observers("Delete both table data or if table did not exist, create table")
        for item in self.__data:
            self.__recipes.append(Recipes(item['id'],item['title'],str(item['readyInMinutes']),str(item['servings']),item['image'] if ('image' in item) else "",str(item['cuisines'],),str(item['dishTypes']),item['instructions'],item['vegetarian'],item['vegan'],item['glutenFree'],item['dairyFree'],item['veryHealthy'],item['cheap'],item['veryPopular']))
            self.__obj.dishInsertOneQuery(self.__recipes[len(self.__recipes)-1])
            self.__obj.nutritionInsertOneQuery(self.__recipes[len(self.__recipes)-1])
            
        self.__obj.notify_observers("recipes Inserted in both table according to columns, ten rows from the objects")
        return self.__recipes
    
    def recipesObjectsUpdate(self):
        self.__obj.dishTableCreator()
        self.__obj.nutritionTableCreation()
        if len(self.__recipes) == len(self.__data):
            for i in range(len(self.__recipes)):
                self.__recipes[i].setId(self.__data[i]['id'])
                self.__recipes[i].setTitle(self.__data[i]['title'])
                self.__recipes[i].setreadyInMinutes(str(self.__data[i]['readyInMinutes']))
                self.__recipes[i].setServings(str(self.__data[i]['servings']))
                self.__recipes[i].setImage(self.__data[i]['image'] if ('image' in self.__data[i]) else "")
                self.__recipes[i].setCuisines(str(self.__data[i]['cuisines']))
                self.__recipes[i].setdishTypes(str(self.__data[i]['dishTypes']))
                self.__recipes[i].setInstructions(self.__data[i]['instructions'])
                self.__recipes[i].setVegetarian(self.__data[i]['vegetarian'])
                self.__recipes[i].setVegan(self.__data[i]['vegan'])
                self.__recipes[i].setGlutenFree(self.__data[i]['glutenFree'])
                self.__recipes[i].setdairyFree(self.__data[i]['dairyFree'])
                self.__recipes[i].setveryHealthy(self.__data[i]['veryHealthy'])
                self.__recipes[i].setCheap(self.__data[i]['cheap'])
                self.__recipes[i].setveryPopular(self.__data[i]['veryPopular'])
                self.__obj.dishInsertOneQuery(self.__recipes[i])
                self.__obj.nutritionInsertOneQuery(self.__recipes[i])
                
            self.__obj.notify_observers("Nutrition table Inserted ten rows")
            self.__obj.notify_observers("Dish table Inserted ten rows")  
            self.__obj.notify_observers("Recipes object list updated")
        else:
            self.recipesObjects()
        return self.__recipes
    
    def userAddObject(self,id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular):
        self.__user.append(User(id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular))
        self.__obj.userInsertOneQuery(self.__user[len(self.__user)-1])
        self.__obj.notify_observers("Add one user dish in table as well as object")
    
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
        self.__obj.userDeleteOneQuery(id)
        self.__obj.notify_observers("Delete one user dish in table as well as object")

    def receipesDeleteAllObject(self):
        self.__recipes.clear()

    def userObjects(self):
        self.__userData = self.__fetcherObj.fetchUserData()
        self.__fetcherObj.notify_observers("User data fetched from table")
        self.__user.clear()
        
        for item in self.__userData:
            self.__user.append(User(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13],item[14]))

        return self.__user
    
