from fastapi import FastAPI
import uvicorn
from Mapper.dataToObject import dataToObject


app = FastAPI()

# connectionObject = Connection()
# cn = connectionObject.conn()
# cursor = cn.cursor()
# cursor.execute("select * from dish")
# data = cursor.fetchall()
# # print(data)
formattedData = []
# for result in data:
#     formattedData.append(result)
obj = dataToObject()
dishDataObj = obj.dishObjects()
nutritionDataObj = obj.nutritionObjects()
for i in range(len(dishDataObj)):
    for j in range(len(nutritionDataObj)):
        if dishDataObj[i].getId()==nutritionDataObj[j].getdishId():
            formattedData.append([dishDataObj[i].getId(),dishDataObj[i].getTitle(),dishDataObj[i].getreadyInMinutes(),dishDataObj[i].getImage(),dishDataObj[i].getCuisines(),dishDataObj[i].getdishTypes(),dishDataObj[i].getInstructions(),dishDataObj[i].getServings(),nutritionDataObj[j].getVegetarian(),nutritionDataObj[j].getVegan(),nutritionDataObj[j].getGlutenFree(),nutritionDataObj[j].getdairyFree(),nutritionDataObj[j].getveryHealthy(),nutritionDataObj[j].getCheap(),nutritionDataObj[j].getveryPopular()])

@app.get("/")
async def root():
    return {"success": "true",
            "status": 200,
            "data": formattedData}

if __name__ == "_main_":
    uvicorn.run(app, host="localhost", port=8080)
