class Nutrition:
    def __init__(self,dishId ,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular):
        self.__dishId = dishId
        self.__vegetarian = vegetarian
        self.__vegan = vegan
        self.__glutenFree = glutenFree
        self.__dairyFree = dairyFree
        self.__veryHealthy = veryHealthy
        self.__cheap = cheap
        self.__veryPopular = veryPopular

    def getdishId(self):
        return self.__dishId
    
    def setdishId(self,dishId):
        self.__dishId = dishId
    
    def getVegetarian(self):
        return self.__vegetarian
    
    def setVegetarian(self,vegetarian):
        self.__vegetarian = vegetarian
    
    def getVegan(self):
        return self.__vegan
    
    def setVegan(self,vegan):
        self.__vegan = vegan
    
    def getGlutenFree(self):
        return self.__glutenFree
    
    def setGlutenFree(self,glutenFree):
        self.__glutenFree = glutenFree
    
    def getdairyFree(self):
        return self.__dairyFree
    
    def setdairyFree(self,dairyFree):
        self.__dairyFree = dairyFree
    
    def getveryHealthy(self):
        return self.__veryHealthy
    
    def setveryHealthy(self,veryHealthy):
        self.__veryHealthy = veryHealthy
    
    def getCheap(self):
        return self.__cheap
    
    def setCheap(self,cheap):
        self.__cheap = cheap
    
    def getveryPopular(self):
        return self.__veryPopular
    
    def setveryPopular(self,veryPopular):
        self.__veryPopular = veryPopular