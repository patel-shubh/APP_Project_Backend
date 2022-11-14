from commonFunction.fetch_api_data import *
from Classes.dishClass import *
from Classes.nutritionClass import *
from Classes.userClass import *
from MySql.queries import *
from observer import Observer


class dataToObject(object):

    _fetcherObj = dataFetcher()
    _observer2 = Observer(_fetcherObj)
    _data = _fetcherObj.fetchApiData()
    _fetcherObj.notify_observers("Parent API data fetched")
    _userData = _fetcherObj.fetchUserData()
    _recipes = []
    _user = []
    _obj = Queries()
    _observer1 = Observer(_obj)

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
        self._data = self._fetcherObj.fetchApiData()
        self._fetcherObj.notify_observers(
            "Parent API data fetched to get new data")

    def recipesObjects(self):
        self._obj.dishTableCreator()
        self._obj.nutritionTableCreation()
        self._obj.notify_observers(
            "Delete both table data or if table did not exist, create table")
        for item in self._data:
            self._recipes.append(Recipes(item['id'], item['title'], str(item['readyInMinutes']), str(item['servings']), item['image'] if ('image' in item) else "", str(item['cuisines'],), str(
                item['dishTypes']), item['instructions'], item['vegetarian'], item['vegan'], item['glutenFree'], item['dairyFree'], item['veryHealthy'], item['cheap'], item['veryPopular']))
            self._obj.dishInsertOneQuery(self._recipes[len(self._recipes)-1])
            self._obj.nutritionInsertOneQuery(
                self._recipes[len(self._recipes)-1])

        self._obj.notify_observers(
            "recipes Inserted in both table according to columns, ten rows from the objects")
        return self._recipes

    def recipesObjectsUpdate(self):
        self._obj.dishTableCreator()
        self._obj.nutritionTableCreation()
        if len(self._recipes) == len(self._data):
            for i in range(len(self._recipes)):
                self._recipes[i].setId(self._data[i]['id'])
                self._recipes[i].setTitle(self._data[i]['title'])
                self._recipes[i].setreadyInMinutes(
                    str(self._data[i]['readyInMinutes']))
                self._recipes[i].setServings(str(self._data[i]['servings']))
                self._recipes[i].setImage(self._data[i]['image'] if (
                    'image' in self._data[i]) else "")
                self._recipes[i].setCuisines(str(self._data[i]['cuisines']))
                self._recipes[i].setdishTypes(str(self._data[i]['dishTypes']))
                self._recipes[i].setInstructions(self._data[i]['instructions'])
                self._recipes[i].setVegetarian(self._data[i]['vegetarian'])
                self._recipes[i].setVegan(self._data[i]['vegan'])
                self._recipes[i].setGlutenFree(self._data[i]['glutenFree'])
                self._recipes[i].setdairyFree(self._data[i]['dairyFree'])
                self._recipes[i].setveryHealthy(self._data[i]['veryHealthy'])
                self._recipes[i].setCheap(self._data[i]['cheap'])
                self._recipes[i].setveryPopular(self._data[i]['veryPopular'])
                self._obj.dishInsertOneQuery(self._recipes[i])
                self._obj.nutritionInsertOneQuery(self._recipes[i])

            self._obj.notify_observers("Nutrition table Inserted ten rows")
            self._obj.notify_observers("Dish table Inserted ten rows")
            self._obj.notify_observers("Recipes object list updated")
        else:
            self.recipesObjects()
        return self._recipes

    def userAddObject(self, id, title, readyInMinutes, servings, image, cuisines, dishTypes, instructions, vegetarian, vegan, glutenFree, dairyFree, veryHealthy, cheap, veryPopular):
        self._user.append(User(id, title, readyInMinutes, servings, image, cuisines, dishTypes,
                          instructions, vegetarian, vegan, glutenFree, dairyFree, veryHealthy, cheap, veryPopular))
        self._obj.userInsertOneQuery(self._user[len(self._user)-1])
        self._obj.notify_observers(
            "Add one user dish in table as well as object")

    def userDeleteObject(self, id):
        index = None
        for i in range(len(self._user)):
            if self._user[i].getId() == id:
                index = i
                break
        if index == None:
            print("index none")
        else:
            del self._user[index]
        self._obj.userDeleteOneQuery(id)
        self._obj.notify_observers(
            "Delete one user dish in table as well as object")

    def receipesDeleteAllObject(self):
        self._recipes.clear()

    def userObjects(self):
        self._userData = self._fetcherObj.fetchUserData()
        self._fetcherObj.notify_observers("User data fetched from table")
        self._user.clear()

        for item in self._userData:
            self._user.append(User(item[0], item[1], item[2], item[3], item[4], item[5], item[6],
                              item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[14]))

        return self._user
