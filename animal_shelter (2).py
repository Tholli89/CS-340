"""Tyler Hollingsworth
   09-25-2022         """

import urllib
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):

    
    def __init__(self, username: str, password: str):
        """Initializing the MongoClient. This helps to access the MongoDB databases and collections."""
        #username = urllib.parse.quote_plus(username)
        #password = urllib.parse.quote_plus(password)
        self.client = MongoClient('mongodb://%s:%s@localhost:38691/AAC' % (username, password))
        self.database = self.client['AAC']
        print(self.client.list_database_names())


    def create(self, data:dict) -> object:        
        """The create in CRUD takes in a dictionary and inserts the corresponding item."""
        if data is not None:
            return self.database.animals.insert_one(data)
        else:
            raise Exception('Nothing to save, because the passed data parameter is empty')

    def read(self, data:dict) -> object:
        """The read in CRUD takes in a dictionary and returns the corresponding items."""
        if data is not None:
            return self.database.animals.find(data,{"_id": False})
        else:
            return self.database.animals.find(data,{"_id": False})
            #raise Exception('Nothing to search, because the passed data parameter is empty')


    def update(self, data:dict, updateData:dict) -> object:
        """The update in CRUD takes in a dictionary to search for and a dicionary with info to update the corresponding item"""
        if data is not None and updateData is not None:
            return self.database.animals.update_one(data, {'$set':updateData})
        else:
            raise Exception('Nothing to update, because the passed data parameter is empty')


    def delete(self, data:dict) -> object:
        """The delete in CRUD takes in a dictionary and removes the corresponding items."""
        if data is not None:
            return self.database.animals.delete_many(data)
        else:
            raise Exception('Nothing to remove, because the passed data parameter is empty')
