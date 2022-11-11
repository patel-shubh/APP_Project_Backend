from fastapi import FastAPI,Request
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
obj = dataToObject()
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


@app.post("/getuser")
async def getUser(info : Request):
    req_info = await info.json()
    obj.userAddObject(req_info['id'],req_info['title'],req_info['getreadyInMinutes'],req_info['imageUrl'],req_info['getCuisines'],req_info['getdishTypes'],req_info['Instructions'],req_info['getServings'],req_info['getVegetarian'],req_info['getVegan'],req_info['getGlutenFree'],req_info['getdairyFree'],req_info['getveryHealthy'],req_info['getCheap'],req_info['getveryPopular'])
    return {
        "status" : "SUCCESS",
        "data" : "User Dish Successfully Added"
    }

if __name__ == "_main_":
    uvicorn.run(app, host="localhost")
