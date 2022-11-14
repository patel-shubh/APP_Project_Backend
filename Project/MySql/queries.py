from Connection.connection import Connection
from commonFunction.constants import *


class Queries(object):
    _connectionObject = Connection()
    _cn = _connectionObject.conn()
    _cursor = _cn.cursor()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Queries, cls).__new__(cls)
        return cls.instance
    # _instance = None

    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        # print("subsriber append in queries")
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)

    def unsubscribe(self, observer):
        self._observers.remove(observer)
    # def __new__(cls):
    #     if cls._instance is None:
    #         print('Creating the object')
    #         cls._instance = super(Queries, cls).__new__(cls)
    #         # Put any initialization here.
    #     return cls._instance

    def dishInsertOneQuery(self, data):
        # print(type(data.getdishTypes()))
        self._cursor.execute("INSERT INTO "+DISH_TABLE+" (id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)",
                             (data.getId(), data.getTitle(), data.getreadyInMinutes(), data.getServings(), data.getImage(), data.getCuisines(), data.getdishTypes(), data.getInstructions()))

    def dishTableCreator(self):
        self._cursor.execute(
            f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{DISH_TABLE}'")
        if self._cursor.fetchone()[0] == 0:
            # print("if123")
            self._cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {DISH_TABLE} (id int,title VARCHAR(255),readyInMinutes VARCHAR(255),servings VARCHAR(255),image VARCHAR(255),cuisines VARCHAR(255),dishTypes VARCHAR(255),instructions VARCHAR(255),PRIMARY KEY (id))")
        else:
            # print("else123")
            self._cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            self._cursor.execute(f"delete from {DISH_TABLE}")
            self._cn.commit()
            self._cursor.execute("SET FOREIGN_KEY_CHECKS=1")
            # print("end123")
    # def dishUpdateOneQuery(self,data):
    #     self._cursor.execute("INSERT INTO "+DISH_TABLE+" (id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)", (data.getId(),data.getTitle(),data.getreadyInMinutes(),data.getImage(),data.getCuisines(),data.getdishTypes(),data.getInstructions(),data.getServings()))

    def nutritionInsertOneQuery(self, data):
        self._cursor.execute("INSERT INTO "+NUTRITION_TABLE+" (dishId ,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)",
                             (data.getId(), data.getVegetarian(), data.getVegan(), data.getGlutenFree(), data.getdairyFree(), data.getveryHealthy(), data.getCheap(), data.getveryPopular()))

    def nutritionTableCreation(self):
        self._cursor.execute(
            f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{NUTRITION_TABLE}'")
        if self._cursor.fetchone()[0] == 0:
            self._cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {NUTRITION_TABLE} (dishId int,vegetarian BOOLEAN,vegan BOOLEAN,glutenFree BOOLEAN,dairyFree BOOLEAN,veryHealthy BOOLEAN,cheap BOOLEAN,veryPopular BOOLEAN,FOREIGN KEY (dishId) REFERENCES dish (id))")
        else:
            self._cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            self._cursor.execute(f"delete from {NUTRITION_TABLE}")
            self._cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    def userInsertOneQuery(self, data):
        # print(data.getId())
        # print(type(data.getdishTypes()))
        self._cursor.execute("INSERT INTO "+USER_TABLE+" (id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)", (data.getId(), data.getTitle(),
                             data.getreadyInMinutes(), data.getServings(), data.getImage(), data.getCuisines(), data.getdishTypes(), data.getInstructions(), data.getVegetarian(), data.getVegan(), data.getGlutenFree(), data.getdairyFree(), data.getveryHealthy(), data.getCheap(), data.getveryPopular()))

    def userDeleteOneQuery(self, id):
        # print(data.getId())
        # print(type(data.getdishTypes()))
        # print(id)
        self._cursor.execute(f"DELETE FROM {USER_TABLE} where id = {id}",)

    def userTableCreator(self):
        # print("inside method")
        self._cursor.execute(
            f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'app_project' AND table_name = '{USER_TABLE}'")
        # print(self._cursor.fetchone()[0])
        if self._cursor.fetchone()[0] == 0:
            # print("inside method")
            self._cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {USER_TABLE} (id int,title VARCHAR(255),readyInMinutes VARCHAR(255),servings VARCHAR(255),image VARCHAR(255),cuisines VARCHAR(255),dishTypes VARCHAR(255),instructions VARCHAR(255),vegetarian BOOLEAN,vegan BOOLEAN,glutenFree BOOLEAN,dairyFree BOOLEAN,veryHealthy BOOLEAN,cheap BOOLEAN,veryPopular BOOLEAN,PRIMARY KEY (id))")
        # else:
        #     self._cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        #     self._cursor.execute(f"delete from {USER_TABLE}")
        #     self._cursor.execute("SET FOREIGN_KEY_CHECKS=1")
