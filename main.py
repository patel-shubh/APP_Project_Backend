from fastapi import FastAPI
from Project.commonFunction.connection import conn
import json
import uvicorn
app = FastAPI()

cn = conn()
cursor = cn.cursor()
cursor.execute("select * from dish")
data = cursor.fetchall()
formattedData = {}
for result in data:
    formattedData[result[0]] = result[1]


@app.get("/")
async def root():
    return {"success": "true",
            "status": 200,
            "data": formattedData}

if __name__ == "_main_":
    uvicorn.run(app, host="localhost", port=8080)
