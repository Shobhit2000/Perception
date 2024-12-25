from pymongo.mongo_client import MongoClient
import configparser
import logging

from .GenerateMongoObjID import GenerateMongoObjID

class MongoDB():
    def __init__(self, mongoURI='mongodb+srv://shobhittulshain:perception12345@perceptioncluster.dhrl3.mongodb.net/?retryWrites=true&w=majority&appName=PerceptionCluster'):
        
        # # Read Configuration Parameters
        # self.config = configparser.ConfigParser()
        # self.config.read('config.ini')

        # self.mongoURI = self.config.get('Database', 'mongoURI')

        self.mongoURI = mongoURI

        # Create a new client and connect to the server
        self.client = MongoClient(self.mongoURI)
        self.db = self.client["perception"]
        self.usersCollection = self.db["dashboard"]

        self.generateMongoObjID = GenerateMongoObjID()

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print("Error Occured while connecting to MongoDB Client" + str(e))
