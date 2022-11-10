from fastapi import FastAPI
from Project.Connection.connection import *
import json
import uvicorn
app = FastAPI()

connectionObject = Connection()
cn = connectionObject.conn()
cursor = cn.cursor()
cursor.execute("select * from dish")
data = cursor.fetchall()
# print(data)
formattedData = []
for result in data:
    formattedData.append(result)


@app.get("/")
async def root():
    return {"success": "true",
            "status": 200,
            "data": formattedData}

if __name__ == "_main_":
    uvicorn.run(app, host="localhost", port=8080)
