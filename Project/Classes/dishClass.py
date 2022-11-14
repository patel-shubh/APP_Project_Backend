class Dish:
    def __init__(self,id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions):
        self.__id = id
        self.__title = title
        self.__readyInMinutes = readyInMinutes
        self.__servings = servings
        self.__image = image
        self.__cuisines = cuisines
        self.__dishTypes = dishTypes
        self.__instructions = instructions

    def getId(self):
        return self.__id
    
    def setId(self,id):
        self.__id = id
    
    def getTitle(self):
        return self.__title
    
    def setTitle(self,title):
        self.__title = title
    
    def getreadyInMinutes(self):
        return self.__readyInMinutes
    
    def setreadyInMinutes(self,readyInMinutes):
        self.__readyInMinutes = readyInMinutes
    
    def getImage(self):
        return self.__image
    
    def setImage(self,image):
        self.__image = image
    
    def getCuisines(self):
        return self.__cuisines
    
    def setCuisines(self,cuisines):
        self.__cuisines = cuisines
    
    def getdishTypes(self):
        return self.__dishTypes
    
    def setdishTypes(self,dishTypes):
        self.__dishTypes = dishTypes
    
    def getInstructions(self):
        return self.__instructions
    
    def setInstructions(self,instructions):
        self.__instructions = instructions
    
    def getServings(self):
        return self.__servings
    
    def setServings(self,servings):
        self.__servings = servings
