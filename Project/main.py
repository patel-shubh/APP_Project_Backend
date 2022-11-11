from fastapi import FastAPI
import uvicorn
from Mapper.dataToObject import dataToObject
from fastapi.middleware.cors import CORSMiddleware
from controller.dishAPI import dishAPI

app = FastAPI()

origins = ["*"]

# Handling CORS Policy 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# connectionObject = Connection()
# cn = connectionObject.conn()
# cursor = cn.cursor()
# cursor.execute("select * from dish")
# data = cursor.fetchall()
# # print(data)
# for result in data:
#     formattedData.append(result)
# formattedData = []
# obj = dataToObject()
# dishDataObj = obj.dishObjects()
# nutritionDataObj = obj.nutritionObjects()
# for i in range(len(dishDataObj)):
#     for j in range(len(nutritionDataObj)):
#         if dishDataObj[i].getId()==nutritionDataObj[j].getdishId():
#             formattedData.append([dishDataObj[i].getId(),dishDataObj[i].getTitle(),dishDataObj[i].getreadyInMinutes(),dishDataObj[i].getImage(),dishDataObj[i].getCuisines(),dishDataObj[i].getdishTypes(),dishDataObj[i].getInstructions(),dishDataObj[i].getServings(),nutritionDataObj[j].getVegetarian(),nutritionDataObj[j].getVegan(),nutritionDataObj[j].getGlutenFree(),nutritionDataObj[j].getdairyFree(),nutritionDataObj[j].getveryHealthy(),nutritionDataObj[j].getCheap(),nutritionDataObj[j].getveryPopular()])

a=dishAPI()
@app.get("/")
async def root():
    return a.getDishes()

if __name__ == "_main_":
    uvicorn.run(app, host="localhost")
