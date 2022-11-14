from fastapi import FastAPI, Request
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


dishApiObj = dishAPI()
userApiObj = userAPI()


@app.get("/")
def getDish():
    return dishApiObj.getDishes()


@app.post("/dish/add/")
async def addUser(info: Request):
    return userApiObj.addUserDish(await info.json())


@app.post("/dish/remove")
async def removeUser(info: Request):
    return userApiObj.deleteUserDish(await info.json())


@app.get("/user/dish")
def userDish():
    return userApiObj.getUserDish()


@app.get("/refresh")
def refreshDish():
    return dishApiObj.getNewDishes()
