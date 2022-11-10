class Dish:
    def __init__(self,id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions):
        self.id = id
        self.title = title
        self.readyInMinutes = readyInMinutes
        self.servings = servings
        self.image = image
        self.cuisines = cuisines
        self.dishTypes = dishTypes
        self.instructions = instructions

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
