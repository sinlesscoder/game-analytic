import pandas as pd
from itertools import combinations
from fuzzywuzzy import fuzz

# Turns a Dataframe into JSON
def create_json_from_df(df, cols):
    subset = df[cols]

    results = []

    for i in range(subset.shape[0]):
        row = subset.iloc[i]
        results.append(row.to_dict())
    
    return results

# Parse Combinations into Filtered DataFrames
def parse_combo_filter_df(df_one: pd.DataFrame, df_two: pd.DataFrame, col_one: str, col_two: str):
    """
    Input: Two dataframe and one column name from each dataframe for merging
    Output: Merged dataframe
    """
    df_two.rename(columns={col_two: col_one}, inplace=True)
    fuzzy_threshold = 90

    object_one = create_json_from_df(df_one, [col_one])
    object_two = create_json_from_df(df_two, [col_one])

    combos = list(filter(lambda x: fuzz.partial_ratio(x[0][col_one], x[1][col_one]) 
    >= fuzzy_threshold, combinations(object_one + object_two, 2)))

    for combo in combos:
        elem_one, elem_two = combo

        fruit_one = elem_one[col_one]
        fruit_two = elem_two[col_one]
        df_two.replace({fruit_two}, fruit_one, inplace=True)
    
    merged_df = df_one.merge(df_two, on=col_one, how='inner')  # 'inner', 'outer', 'left', or 'right'

    return merged_df