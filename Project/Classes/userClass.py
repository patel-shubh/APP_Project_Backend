class User:
    def __init__(self,id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular):
        self.id = id
        self.title = title
        self.readyInMinutes = readyInMinutes
        self.servings = servings
        self.image = image
        self.cuisines = cuisines
        self.dishTypes = dishTypes
        self.instructions = instructions
        self.vegetarian = vegetarian
        self.vegan = vegan
        self.glutenFree = glutenFree
        self.dairyFree = dairyFree
        self.veryHealthy = veryHealthy
        self.cheap = cheap
        self.veryPopular = veryPopular

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
    
    def getTitle(self):
        return self.title
    
    def setTitle(self,title):
        self.title = title
    
    def getreadyInMinutes(self):
        return self.readyInMinutes
    
    def setreadyInMinutes(self,readyInMinutes):
        self.readyInMinutes = readyInMinutes
    
    def getImage(self):
        return self.image
    
    def setImage(self,image):
        self.image = image
    
    def getCuisines(self):
        return self.cuisines
    
    def setCuisines(self,cuisines):
        self.cuisines = cuisines
    
    def getdishTypes(self):
        return self.dishTypes
    
    def setdishTypes(self,dishTypes):
        self.dishTypes = dishTypes
    
    def getInstructions(self):
        return self.instructions
    
    def setInstructions(self,instructions):
        self.instructions = instructions
    
    def getServings(self):
        return self.servings
    
    def setServings(self,servings):
        self.servings = servings
    
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
