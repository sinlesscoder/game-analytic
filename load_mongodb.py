from rapidapi import retrieve_item_pages
from pymongo import MongoClient
from json_read import json_reader

# Connection to MongoDB
def retrieve_mongo_connection(collection_name: str, database_name: str):
    """
    Inputs:
        - search_term (string): Search term for the query of API
        - uri (string): Uniform Resource Identifier to represent MongoDB server
    
    Output:
        - collection_name (Mongo.Collection): Collection to store your results.
    """

    # Accessing JSON
    uri = json_reader("Local_MongoDB")

    # Set up a Mongo Client
    client = MongoClient(uri)

    # Create a database
    database = client[database_name]

    # Create a collection
    collection = database[collection_name]

    return collection

def retrieve_all_collections(database_name: str) -> dict:
    uri = json_reader("Local_MongoDB")

    # Set up a Mongo Client
    client = MongoClient(uri)

    # Create a database
    database = client[database_name]

    # See all the collections
    results = database.list_collection_names()

    # Dictionary for All Collections
    col_dict = {col: [obj for obj in col.find()] for col in results}

    return col_dict
