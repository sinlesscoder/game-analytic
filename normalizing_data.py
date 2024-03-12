import pandas as pd
from load_mongodb import retrieve_mongo_connection
from pymongo import MongoClient
from json_read import json_reader


# Helper Function: Normalize Collection
def normalize_collection(col_name: str, db_name: str):
    # Retrieving the collection from Mongo Client
    col = retrieve_mongo_connection(col_name, db_name)

    # Retrieve all documents in the collection
    docs = [obj for obj in col.find()]

    # Transform the JSON into a DataFrame
    df = pd.json_normalize(docs)

    return df

# Normalizing multiple Collection in a Database into one Pandas Dataframe
def data_model(database: str):
    uri = json_reader("Local_MongoDB")
    frames = []

    # Connecting to Mongo
    client = MongoClient(uri)
    db = client[database]

    collection_names = db.list_collection_names()

    # Appending each collection into a 'frames' list
    for name in collection_names:
       collection = db[name]
       list_col = collection.find()
       for document in list_col:
           frames.append(document)
    
    # Converting into Pandas Dataframe
    df = pd.json_normalize(frames)

    return df

