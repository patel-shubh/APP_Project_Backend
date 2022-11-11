from Mapper.dataToObject import dataToObject

class userAPI:
    
    obj = dataToObject()
    # addUserObjs = obj.userAddObject()
    # deleteUserObjs = obj.userAddObject()
    # getUserObjs = obj.userObjects()

    def addUserDish(self,info):
        req_info = info.json()
        # print(req_info)
        self.obj.userAddObject(req_info['id'],req_info['title'],req_info['getreadyInMinutes'],str(req_info['getServings']),req_info['imageUrl'],req_info['getCuisines'],req_info['getdishTypes'],req_info['Instructions'],req_info['getVegetarian'],req_info['getVegan'],req_info['getGlutenFree'],req_info['getdairyFree'],req_info['getveryHealthy'],req_info['getCheap'],req_info['getveryPopular'])

        return {"success": "true",
                "status": 200,
                "data": "User Dish Successfully Added"}
    
    def deleteUserDish(self,info):
        req_info = info.json()
        self.obj.deleteUserObjs(req_info['id'])

        return {"success": "true",
                "status": 200,
                "data": "User Dish Successfully Added"}

    def getUserDish(self):
        formattedData = []
        for i in range(len(self.obj.getUserObjs)):
            formattedData.append({"id": self.userObjs[i].getId(), "title": self.userObjs[i].getTitle(), "getreadyInMinutes": self.userObjs[i].getreadyInMinutes(), "imageUrl": self.userObjs[i].getImage(), "getCuisines": self.userObjs[i].getCuisines(), "getdishTypes": self.userObjs[i].getdishTypes(), "Instructions": self.userObjs[i].getInstructions(), "getServings": self.userObjs[i].getServings(
                        ), "getVegetarian": self.userObjs[i].getVegetarian(), "getVegan": self.userObjs[i].getVegan(), "getGlutenFree": self.userObjs[i].getGlutenFree(), "getdairyFree": self.userObjs[i].getdairyFree(), "getveryHealthy": self.userObjs[i].getveryHealthy(), "getCheap": self.userObjs[i].getCheap(), "getveryPopular": self.userObjs[i].getveryPopular()})
        return {"success": "true",
                "status": 200,
                "data": formattedData}
    
    

    