import logging

def widget_mapper(record, mongoDB):
    widget_record = {}

    widget_record['_id'] = mongoDB.generateMongoObjID.generate_custom_object_id()

    if record.get('file_id'):
        widget_record['file_id'] = record.get('file_id')

    if record.get('widget_name'):
        widget_record['widget_name'] = record.get('widget_name')
    
    if record.get('colour'):
        widget_record['colour'] = record.get('colour')
    
    if record.get('graph_type'):
        widget_record['graph_type'] = record.get('graph_type')

    if record.get('query'):
        widget_record['query'] = record.get('query')

    if record.get('center_x'):
        widget_record['center_x'] = record.get('center_x')

    if record.get('center_y'):
        widget_record['center_y'] = record.get('center_y')

    if record.get('height'):
        widget_record['height'] = record.get('height')

    if record.get('width'):
        widget_record['width'] = record.get('width')

    if record.get('data'):
        widget_record['data'] = record.get('data')

    return widget_record

def dashboard_mapper(record, mongoDB):
    '''
    This Function maps the Users object with approriate keys and creates the json to be inserted in the DB
    
    Args:
        record: Dictonary containing the key value pairs required for Users object
    
    Returns:
        dictionary: Mapped dictonary containing the key value pairs required for Users object
    '''

    dashboard_record = {}
    
    # Manually generate the MongoDB Object_ID
    dashboard_record['_id'] = mongoDB.generateMongoObjID.generate_custom_object_id()
    
    if record.get('dashboard_name'):
        dashboard_record['dashboard_name'] = record.get('dashboard_name')

    if record.get('user_id'):
        dashboard_record['user_id'] = record.get('user_id')
    
    if record.get('colour'):
        dashboard_record['colour'] = record.get('colour')
    
    if record.get('refresh_time'):
        dashboard_record['refresh_time'] = record.get('refresh_time')
    
    if record.get('creation_tms'):
        dashboard_record['creation_tms'] = record.get('creation_tms')
    
    if record.get('last_update_tms'):
        dashboard_record['last_update_tms'] = record.get('last_update_tms')
    
    if record.get('widgets'):
        tmp = []
        for i in record.get('widgets'):
            tmp.append(widget_mapper(i, mongoDB))
        
        dashboard_record['widgets'] = tmp


    logging.info('Mapped Record object !!')
    return dashboard_record

def add_dashboard(record, mongoDB):
    """
    Function to add a single User in MongoDB

    Args:
        record (dict): Dictonary containing the key value pairs required for Users object
        mongoDB (object): mongo client for performing database operations

    Returns:
        response(obj): User_id object if the insert was successful else error msg
    """

    try:
        record = dashboard_mapper(record, mongoDB)

        # if user exists with provided email Raise Exception
        inserted_object = mongoDB.usersCollection.insert_one(record)
        
        response = inserted_object.inserted_id
        logging.info('Record Inserted !!')
        return response
    
    except Exception as e:
        response = 'Insert failed with error:- ' + str(e)
        logging.error(response)
        raise Exception(response)


def delete_dashboard(dashboard_id, mongoDB):
    """
    Function to delete a dashboard

    Args:
        dashboard_id (String): dashboard_id to be deleted
        mongoDB (object): mongo client for performing database operations

    Returns:
        response(String): Msg stating whether the user was deleted or if there was an error
    """

    try:
        mongoDB.dashboardsCollection.delete_one({'_id' : dashboard_id})
        
        response = "Record Deleted !!"
        logging.info(response)
        return response
    
    except Exception as e:
        response = 'Delete failed with error:- ' + str(e)
        logging.error(response)
        raise Exception(response)


def update_dashboard(dashboard_id, updated_record, mongoDB):
    """
    Function to update a dashboard

    Args:
        dashboard_id (String): dashboard for which the user is to be updated
        updatedRecord (dict): dictionary of dashboard data which is to be updated
        mongoDB (object): mongo client for performing database operations

    Returns:
        response(String): response msg
    """

    try:
        updated_record = dashboard_mapper(updated_record, mongoDB)
        mongoDB.dashboardsCollection.update_one({'_id' : dashboard_id}, {"$set": updated_record}, upsert=False)
        
        response = 'Record Updated !!'
        logging.info(response)
        return response
    
    except Exception as e:
        response = 'Update failed with error:- ' + str(e)
        logging.error(response)
        raise Exception(response)


def find_all_dashboard(user_id, mongoDB):
    """
    Function to find all dashboards for a user

    Args:
        user_id (String): user_id for which the dashboard is to be searched
        mongoDB (object): mongo client for performing database operations

    Returns:
        response(dict): dictionary if a record is found else error msg
    """
    
    try:
        record = mongoDB.dashboardsCollection.find_one({'user_id': user_id})
    
        response = record
        logging.info('Record Found with details:- %s', str(record))
        return response
    
    except Exception as e:
        response = 'Finding Record failed with error:- ' + str(e)
        logging.error(response)
        raise Exception(response)


def close_mongo_client(mongoDB):
    mongoDB.client.close()
    logging.info('Mongo client closed')