from commonFunction.fetch_api_data import *
from Connection.connection import Connection
from commonFunction.constants import *
import sys
sys.setrecursionlimit(10**7)



def insertTable():
    connectionObject = Connection()
    cn = connectionObject.conn()
    cursor = cn.cursor()
    recipes  = fetchApiData()
    dishArray = []
    nutritionArray = []
    i = 0
    for item in recipes:
        temp = (item['id'],item['vegetarian'],item['vegan'],item['glutenFree'],item['dairyFree'],item['veryHealthy'],item['cheap'],item['veryPopular'])
        nutritionArray.insert(i,temp)
        temp = (item['id'],item['title'],item['readyInMinutes'],item['servings'],item['image'],str(item['cuisines']),str(item['dishTypes']),item['instructions'])
        dishArray.insert(i,temp)
        i = i+1
    i=0
    # print(dishArray)
    # print(type(finalTuple))
    cursor.execute(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{DISH_TABLE}'")
    if cursor.fetchone()[0]==0:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {DISH_TABLE} (id int,title VARCHAR(255),readyInMinutes VARCHAR(255),servings VARCHAR(255),image VARCHAR(255),cuisines VARCHAR(255),dishTypes VARCHAR(255),instructions VARCHAR(255),PRIMARY KEY (id))")
        cursor.executemany("INSERT INTO "+DISH_TABLE+" (id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions) VALUES (%s, %s,%s, %s,%s, %s,%s,%s)", dishArray)
    else:
        cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute(f"delete from {DISH_TABLE}")
        cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        cursor.executemany("INSERT INTO "+DISH_TABLE+" (id,title,readyInMinutes,servings,image,cuisines,dishTypes,instructions) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)", dishArray)
    # cursor.commit()

    # print(finalTuple)
    # print(type(finalTuple))
    cursor.execute(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{NUTRITION_TABLE}'")
    if cursor.fetchone()[0]==0:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {NUTRITION_TABLE} (dishId int,vegetarian BOOLEAN,vegan BOOLEAN,glutenFree BOOLEAN,dairyFree BOOLEAN,veryHealthy BOOLEAN,cheap BOOLEAN,veryPopular BOOLEAN,FOREIGN KEY (dishId) REFERENCES dish (id))")
        cursor.executemany("INSERT INTO "+NUTRITION_TABLE+" (dishId ,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)", nutritionArray)
    else:
        cursor.execute("SET FOREIGN_KEY_CHECKS=0")
        cursor.execute(f"delete from {NUTRITION_TABLE}")
        cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        cursor.executemany("INSERT INTO "+NUTRITION_TABLE+" (dishId ,vegetarian ,vegan ,glutenFree ,dairyFree ,veryHealthy ,cheap ,veryPopular) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)", nutritionArray)

    

