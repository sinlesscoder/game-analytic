import pandas as pd
from sqlalchemy import create_engine
from getpass import getpass
from json_read import json_reader

keys = json_reader("POSTGRES_PASSWORD")

# Insert to the Postgres database
def postgres_insertion(df: pd.DataFrame, table_name:str):
    username = 'postgres'
    password = getpass("Type in your server password: ")
    host = 'localhost'
    port = '5432'
    database = 'project'

    # Dialect together: Example PostgreSQL
    dialect = f'postgresql://{username}:{password}@{host}:{port}/{database}'

    # Create the engine object
    engine = create_engine(dialect)

    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

    print("Data inserted successfully.")

# Read a table from Postgres database
def postgres_data(table_name:str):
    username = 'postgres'
    password = keys #getpass("Type in your server password: ")
    host = 'localhost'
    port = '5432'
    database = 'project'

    # Dialect together: Example PostgreSQL
    dialect = f'postgresql://{username}:{password}@{host}:{port}/{database}'
    
    # Create the engine object
    engine = create_engine(dialect)

    # Fetch data from the specified table into a Pandas DataFrame
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql(query, engine)

    return df
