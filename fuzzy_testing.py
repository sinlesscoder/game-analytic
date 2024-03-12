import pandas as pd
from normalizing_data import normalize_collection, data_model
from postgres_conn import postgres_insertion
from merging_tools import parse_combo_filter_df
from os import getcwd

# Backlog Gaming Data Path
backlog_game_path = getcwd() 

# Sample object
cheapshark_df = data_model('cheapshark')
backlog_df = pd.read_csv(f"{backlog_game_path}/backloggd_games.csv", chunksize=1000)
backlog_chunks = list(backlog_df)
backlog_df = normalize_collection('backlog_col', 'Database_1')

# List to store results
results = []

# Loop through all the chunks and apply fuzzywuzzy logic
for i, chunk in enumerate(backlog_chunks):
    # Apply fuzzy wuzzy function
    result_df = parse_combo_filter_df(cheapshark_df, chunk, 'title', 'Title')
    # Append the DataFrame to the results list
    results.append(result_df)

    print(f"Chunk {i+1} processed.")

# Quick Analytics by Concatenating all into a single DataFrame
final_df = pd.concat(results) 

print(final_df.shape)

# dropping irrelevant columns
final_df = final_df.drop(['_id','dealID', 'storeID', 'isOnSale', 'savings', 'releaseDate', 'lastChange', 'dealRating', 'Unnamed: 0'], axis=1)
final_df = final_df.drop_duplicates(subset=['title','gameID'])

postgres_insertion(final_df, 'merged_game_data')
