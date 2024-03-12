from load_mongodb import retrieve_mongo_connection
from rapidapi import cheapshark_game_deals

# Select a search term
terms = ['batman', 'infamous', 'spider-man', 'marvel', 'injustice']

def insert_data(search_terms: list, database:str):

    for term in search_terms:
        data = cheapshark_game_deals(term,1)
        col = retrieve_mongo_connection(term, database)
        col.insert_many(data)
    print("Insertion successful")

insert_data(terms,'cheapshark')