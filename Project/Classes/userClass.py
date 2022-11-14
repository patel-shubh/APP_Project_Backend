class User:
    def __init__(self, id, title, readyInMinutes, servings, image, cuisines, dishTypes, instructions, vegetarian, vegan, glutenFree, dairyFree, veryHealthy, cheap, veryPopular):
        self._id = id
        self._title = title
        self._readyInMinutes = readyInMinutes
        self._servings = servings
        self._image = image
        self._cuisines = cuisines
        self._dishTypes = dishTypes
        self._instructions = instructions
        self._vegetarian = vegetarian
        self._vegan = vegan
        self._glutenFree = glutenFree
        self._dairyFree = dairyFree
        self._veryHealthy = veryHealthy
        self._cheap = cheap
        self._veryPopular = veryPopular

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

    def getVegetarian(self):
        return self._vegetarian

    def setVegetarian(self, vegetarian):
        self._vegetarian = vegetarian

    def getVegan(self):
        return self._glutenFree

    def setVegan(self, vegan):
        self._vegan = vegan

    def getGlutenFree(self):
        return self._glutenFree

    def setGlutenFree(self, glutenFree):
        self._glutenFree = glutenFree

    def getdairyFree(self):
        return self._dairyFree

    def setdairyFree(self, dairyFree):
        self._dairyFree = dairyFree

    def getveryHealthy(self):
        return self._veryHealthy

    def setveryHealthy(self, veryHealthy):
        self._veryHealthy = veryHealthy

    def getCheap(self):
        return self._cheap

    def setCheap(self, cheap):
        self._cheap = cheap

    def getveryPopular(self):
        return self._veryPopular

    def setveryPopular(self, veryPopular):
        self._veryPopular = veryPopular
