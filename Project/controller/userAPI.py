from Mapper.dataToObject import dataToObject

class userAPI:
    
    obj = dataToObject()
    # addUserObjs = obj.userAddObject()
    # deleteUserObjs = obj.userAddObject()
    # getUserObjs = obj.userObjects()

    def addUserDish(self,req_info):
        # req_info = info.json()
        # print(info)
        self.obj.userAddObject(req_info['id'],req_info['title'],req_info['getreadyInMinutes'],str(req_info['getServings']),req_info['imageUrl'],req_info['getCuisines'],req_info['getdishTypes'],req_info['Instructions'],req_info['getVegetarian'],req_info['getVegan'],req_info['getGlutenFree'],req_info['getdairyFree'],req_info['getveryHealthy'],req_info['getCheap'],req_info['getveryPopular'])
        return {"success": "true",
                "status": 200,
                "data": "User Dish Successfully Added"}
    
    def deleteUserDish(self,req_info):
        self.obj.userDeleteObject(req_info['id'])
        return {"success": "true",
                "status": 200,
                "data": "User Dish Successfully Deleted"}

    def getUserDish(self):
        formattedData = []
        userObj = self.obj.userObjects()
        for i in range(len(userObj)):
            formattedData.append({"id": userObj[i].getId(), "title": userObj[i].getTitle(), "getreadyInMinutes": userObj[i].getreadyInMinutes(), "getServings": userObj[i].getServings(
                        ), "imageUrl": userObj[i].getImage(), "getCuisines": userObj[i].getCuisines(), "getdishTypes": userObj[i].getdishTypes(), "Instructions": userObj[i].getInstructions(), "getVegetarian": userObj[i].getVegetarian(), "getVegan": userObj[i].getVegan(), "getGlutenFree": userObj[i].getGlutenFree(), "getdairyFree": userObj[i].getdairyFree(), "getveryHealthy": userObj[i].getveryHealthy(), "getCheap": userObj[i].getCheap(), "getveryPopular": userObj[i].getveryPopular()})
        return {"success": "true",
                "status": 200,
                "data": formattedData}
    
    

    