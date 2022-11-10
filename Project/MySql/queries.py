from Connection.connection import Connection
from commonFunction.constants import *

connectionObject = Connection()
cn = connectionObject.conn()
cursor = cn.cursor()

class Queries:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Queries, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
    
    def dishInsertOneQuery(self,data):
        # print(type(data.getdishTypes()))
        cursor.execute("INSERT INTO "+DISH_TABLE+" (id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)", (data.getId(),data.getTitle(),data.getreadyInMinutes(),data.getImage(),data.getCuisines(),data.getdishTypes(),data.getInstructions(),data.getServings()))
    
    def dishTableCreator(self):
        cursor.execute(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{DISH_TABLE}'")
        if cursor.fetchone()[0]==0:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {DISH_TABLE} (id int,title VARCHAR(255),readyInMinutes VARCHAR(255),servings VARCHAR(255),image VARCHAR(255),cuisines VARCHAR(255),dishTypes VARCHAR(255),instructions VARCHAR(255),PRIMARY KEY (id))")
        else:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            cursor.execute(f"delete from {DISH_TABLE}")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    # def dishUpdateOneQuery(self,data):
    #     cursor.execute("INSERT INTO "+DISH_TABLE+" (id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)", (data.getId(),data.getTitle(),data.getreadyInMinutes(),data.getImage(),data.getCuisines(),data.getdishTypes(),data.getInstructions(),data.getServings()))
   
    def nutritionInsertOneQuery(self,data):
        cursor.execute("INSERT INTO "+NUTRITION_TABLE+" (dishId ,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)", (data.getdishId(),data.getVegetarian(),data.getVegan(),data.getGlutenFree(),data.getdairyFree(),data.getveryHealthy(),data.getCheap(),data.getveryPopular()))

    def nutritionTableCreation(self):
        cursor.execute(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{NUTRITION_TABLE}'")
        if cursor.fetchone()[0]==0:
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {NUTRITION_TABLE} (dishId int,vegetarian BOOLEAN,vegan BOOLEAN,glutenFree BOOLEAN,dairyFree BOOLEAN,veryHealthy BOOLEAN,cheap BOOLEAN,veryPopular BOOLEAN,FOREIGN KEY (dishId) REFERENCES dish (id))")
        else:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            cursor.execute(f"delete from {NUTRITION_TABLE}")
            cursor.execute("SET FOREIGN_KEY_CHECKS=1")
