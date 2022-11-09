import mysql.connector as connector


# def conn():
#     mdb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database = "app_project"
#     )
#     cursor = mdb.cursor()
#     return cursor

def conn():

    config = {
        "host":"localhost",
        "user":"root",
        "password":"",
        "database": "app_project"
    }
    try:
        c = connector.connect(autocommit = True,**config)
        return c
    except:
        print("connection error")
        exit(1)


 