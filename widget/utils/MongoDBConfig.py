# from pymongo.mongo_client import MongoClient
# import configparser
# import logging

# from .GenerateMongoObjID import GenerateMongoObjID

# class MongoDB():
#     def __init__(self):
        
#         # Read Configuration Parameters
#         self.config = configparser.ConfigParser()
#         self.config.read('config.ini')

#         self.mongoURI = self.config.get('Database', 'mongoURI')

#         # Create a new client and connect to the server
#         self.client = MongoClient(self.mongoURI)
#         self.db = self.client["Perception"]
#         self.usersCollection = self.db["Widget"]

#         self.generateMongoObjID = GenerateMongoObjID()

#         # Send a ping to confirm a successful connection
#         try:
#             self.client.admin.command('ping')
#             logging.info("Pinged your deployment. You successfully connected to MongoDB!")
#         except Exception as e:
#             logging.error("Error Occured while connecting to MongoDB Client" + str(e))
