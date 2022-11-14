from fastapi import FastAPI,Request
import uvicorn
from Mapper.dataToObject import dataToObject
from fastapi.middleware.cors import CORSMiddleware
from controller.dishAPI import dishAPI
from controller.userAPI import userAPI

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

dishApiObj=dishAPI()
userApiObj=userAPI()

@app.get("/")
def getDish():
    return dishApiObj.getDishes()

@app.post("/dish/add/")
async def addUser(info : Request):
    return userApiObj.addUserDish(await info.json())

@app.post("/dish/remove")
async def removeUser(info : Request):
    return userApiObj.deleteUserDish(await info.json())
    
@app.get("/user/dish")
def userDish():
    return userApiObj.getUserDish()

@app.get("/refresh")
def refreshDish():
    return dishApiObj.getNewDishes()

