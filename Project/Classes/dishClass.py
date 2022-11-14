class Dish:
    def __init__(self, id, title, readyInMinutes, servings, image, cuisines, dishTypes, instructions):
        self._id = id
        self._title = title
        self._readyInMinutes = readyInMinutes
        self._servings = servings
        self._image = image
        self._cuisines = cuisines
        self._dishTypes = dishTypes
        self._instructions = instructions

    def getId(self):
        return self._id

    def setId(self, id):
        self._id = id

    def getTitle(self):
        return self._title

    def setTitle(self, title):
        self._title = title

    def getreadyInMinutes(self):
        return self._readyInMinutes

    def setreadyInMinutes(self, readyInMinutes):
        self._readyInMinutes = readyInMinutes

    def getImage(self):
        return self._image

    def setImage(self, image):
        self._image = image

    def getCuisines(self):
        return self._cuisines

    def setCuisines(self, cuisines):
        self._cuisines = cuisines

    def getdishTypes(self):
        return self._dishTypes

    def setdishTypes(self, dishTypes):
        self._dishTypes = dishTypes

    def getInstructions(self):
        return self._instructions

    def setInstructions(self, instructions):
        self._instructions = instructions

    def getServings(self):
        return self._servings

    def setServings(self, servings):
        self._servings = servings
