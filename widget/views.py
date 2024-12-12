# from django.shortcuts import render
# import pymongo
# from .MongoDBConfig import MongoDB

# client = MongoDB('mongodb+srv://username:password@HOSTNAME/DATABASE_NAME?authSource=admin&tls=true&tlsCAFile=<PATH_TO_CA_FILE>')

# @chats_bp.route('/addNewChat', methods=['POST'])
# def addNewChat():
#     """
#     Endpoint to add a new Chat in MongoDB

#     Returns:
#         json: json response stating whether the data was inserted or if there was an error
#     """
    
#     try:
#         newRecord = request.json['newRecord']
#         mongoDB = current_app.config['mongoDB']
        
#         # Call DatabaseOPs function to insert new chat
#         insertedObject = Chats.addNewChat(newRecord, mongoDB)

#         logging.info('Record Inserted !!')
#         response = str(insertedObject)

#     except Exception as e:
#         response = 'Insert failed with error:- ' + str(e)
#         logging.error(response)
    
#     return jsonify({"response":response})


# @chats_bp.route('/deleteChat', methods=['POST'])
# def deleteChat():
#     """
#     Endpoint to delete a single Chat in MongoDB

#     Returns:
#         json: json response stating whether a single Chat was deleted or if there was an error
#     """

#     try:
#         chatIdToBeDeleted = ObjectId(request.json['chatIdToBeDeleted'])
#         mongoDB = current_app.config['mongoDB']

#         # Call DatabaseOPs function to delete a chat
#         response = Chats.deleteChat(chatIdToBeDeleted, mongoDB)
#         logging.info('Record Deleted !!')
    
#     except Exception as e:
#         response = 'Delete failed with error:- ' + str(e)
#         logging.error(response)
    
#     return jsonify({"response":response})


# @chats_bp.route('/deleteAllChats', methods=['POST'])
# def deleteAllChats():
#     """
#     Endpoint to delete all Chats in MongoDB

#     Returns:
#         json: json response stating whether all Chats were deleted or if there was an error
#     """

#     try:
#         userEmail = request.json['userEmail']
#         mongoDB = current_app.config['mongoDB']
        
#         # Call DatabaseOPs function to delete all chats of a user
#         response = Chats.deleteAllChats(userEmail, mongoDB)
#         logging.info('All Chat Records Deleted !!')
    
#     except Exception as e:
#         response = 'Delete all failed with error:- ' + str(e)
#         logging.error(response)
    
#     return jsonify({"response":response})

# @chats_bp.route('/updateChat', methods=['PUT'])
# def updateChat():
#     """
#     Endpoint to update a single Chat in MongoDB

#     Returns:
#         json: json response stating whether a single Chat was updated or if there was an error
#     """

#     try:
#         req = request.json
#         chatIdToBeUpdated = ObjectId(req['chatIdToBeUpdated'])
#         updatedRecord = req['updatedRecord']
#         mongoDB = current_app.config['mongoDB']

#         # Call DatabaseOPs function to update a chatline
#         response = Chats.updateChats(chatIdToBeUpdated, updatedRecord, mongoDB)
#         logging.info('Record Updated !!')
    
#     except Exception as e:
#         response = 'Update failed with error:- %s', str(e)
#         logging.error(response)
    
#     return jsonify({"response":response})


# @chats_bp.route('/findChat', methods=['GET'])
# def findExistingChat():
#     """
#     Endpoint to find an Chat in MongoDB

#     Returns:
#         json: json response stating whether a single Chat was found or if there was an error
#     """

#     try:
#         chatIdToBeSearched = ObjectId(request.json['chatIdToBeSearched'])
#         mongoDB = current_app.config['mongoDB']

#         record = Chats.findExistingChat(chatIdToBeSearched, mongoDB)
#         record['_id'] = str(record['_id'])
        
#         logging.info('Record Found with details:- %s', str(record))
#         response = record
    
#     except Exception as e:
#         response = 'Finding Record failed with error:- ' + str(e)
#         logging.error(response)
    
#     return jsonify({"response":response})


# @chats_bp.route('/findAllChats', methods=['GET'])
# def findAllExistingChats():
#     """
#     Endpoint to find all Chats in MongoDB using email_id

#     Returns:
#         json: json response stating whether all Chats were found or if there was an error
#     """

#     try:
#         userEmail = request.json['userEmail']
#         mongoDB = current_app.config['mongoDB']
        
#         # Call DatabaseOPs function to delete all chatlines in a chatId
#         records = Chats.findAllExistingChats(userEmail, mongoDB)

#         for record in records:
#             record['_id'] = str(record['_id'])

#         logging.info('Record Found with details:- %s', str(records))
#         response = records
    
#     except Exception as e:
#         response = 'Finding Records failed with error:- ' + str(e)
#         logging.error(response)
    
#     return jsonify({"response":response})


# # def closeMongoCLient(self):
# #     mongoDB.client.close()
# #     logging.info('Mongo client closed')