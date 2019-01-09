###############################################################################################
# small features for the managemement of our database
###############################################################################################

# list of import
import json

# Check if all the parameters are define properly for the connection
def checkParams():
    try:
        with open("dbparam.json") as json_data:
            myData=json.load(json_data)
            #myCon,myDatabase=myData['myCon'],myData['myDatabase']
            myCon=myData["myCon"]
            #check if all the fields are populated
            if (myCon != "" and myDatabase != "" ):
                return True
            else:
                return False
    except:
        return False

# Return all the parameters for the connection string to the database
def returnParameter():
    if checkParams:
        with open("dbparam.json") as json_data:
            myData=json.load(json_data)
            return myData["myCon"],myData["myDatabase"]
