from Classes.dishClass import Dish


class Recipes(Dish):
    def __init__(self, id, title, readyInMinutes, servings, image, cuisines, dishTypes, instructions, vegetarian, vegan, glutenFree, dairyFree, veryHealthy, cheap, veryPopular):
        super().__init__(id, title, readyInMinutes, servings,
                         image, cuisines, dishTypes, instructions)
        self._vegetarian = vegetarian
        self._vegan = vegan
        self._glutenFree = glutenFree
        self._dairyFree = dairyFree
        self._veryHealthy = veryHealthy
        self._cheap = cheap
        self._veryPopular = veryPopular

    def getVegetarian(self):
        return self._vegetarian

    def setVegetarian(self, vegetarian):
        self._vegetarian = vegetarian

    def getVegan(self):
        return self._vegan

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
