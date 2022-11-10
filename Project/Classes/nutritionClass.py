class Nutrition:
    def __init__(self,dishId ,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular):
        self.dishId = dishId
        self.vegetarian = vegetarian
        self.vegan = vegan
        self.glutenFree = glutenFree
        self.dairyFree = dairyFree
        self.veryHealthy = veryHealthy
        self.cheap = cheap
        self.veryPopular = veryPopular

    def getdishId(self):
        return self.dishId
    
    def setdishId(self,dishId):
        self.dishId = dishId
    
    def getVegetarian(self):
        return self.vegetarian
    
    def setVegetarian(self,vegetarian):
        self.vegetarian = vegetarian
    
    def getVegan(self):
        return self.glutenFree
    
    def setVegan(self,vegan):
        self.vegan = vegan
    
    def getGlutenFree(self):
        return self.glutenFree
    
    def setGlutenFree(self,glutenFree):
        self.glutenFree = glutenFree
    
    def getdairyFree(self):
        return self.dairyFree
    
    def setdairyFree(self,dairyFree):
        self.dairyFree = dairyFree
    
    def getveryHealthy(self):
        return self.veryHealthy
    
    def setveryHealthy(self,veryHealthy):
        self.veryHealthy = veryHealthy
    
    def getCheap(self):
        return self.cheap
    
    def setCheap(self,cheap):
        self.cheap = cheap
    
    def getveryPopular(self):
        return self.veryPopular
    
    def setveryPopular(self,veryPopular):
        self.veryPopular = veryPopular