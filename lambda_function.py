import os
from pymongo import MongoClient


client = MongoClient(host=os.environ.get("ATLAS_URI"))


def lambda_handler(event, context):
    # Name of database
    db = client.test 

    # Name of collection
    collection = db.test 
    
    # Document to add inside
    document = {"first name": "Anaiya", "last name": "Raisinghani"}


    # Insert document
    result = collection.insert_one(document)


    if result.inserted_id:
        return "Document inserted successfully"
    else:
        return "Failed to insert document"