# Superhero Video Game Analytics Project

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzN0ZHJ2ZGQ4M2J0MnFveG84dXZvZmtsdjkxanNnb3R5eW13c3JuaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5Pb4DewIvYo4o/giphy.gif" width="200" height="200" />

This portfolio project aims to analyze video gaming data focusing on superhero-themed games, exploring aspects such as sales price, release date, game ID, reviews, and more. The project employs Pandasai, a Pandas-based library, to assist in analyzing and deriving insights from the gathered gaming data.

## Objective

The primary objective of this project is to conduct comprehensive analytics on video gaming data associated with superhero-themed games. Key goals include:

- Analyzing sales performance based on factors like price, release date, and game ID.
- Evaluating user reviews and their impact on game popularity.
- Deriving insights to aid in understanding market trends and informing game development strategies.

## Data Analysis Process
 
### Data Collection
- Gathering video gaming data related to superhero, from sources like RapidAPI and Kaggle.
- Structuring and organizing the collected data to facilitate analysis.

### Data Cleaning and Merging
- Cleaning the raw gaming data, and ensuring data integrity and consistency.
- Originally in a JSON format for the data from RapidAPI, so I converted them into Pandas DataFrame.
```python
    # Appending each collection into a 'frames' list
    for name in collection_names:
       collection = db[name]
       list_col = collection.find()
       for document in list_col:
           frames.append(document)
    
    # Converting into Pandas Dataframe
    df = pd.json_normalize(frames)

```
- Merged the two datasets using a library called FuzzyWuzzy.
```python
    combos = list(filter(lambda x: fuzz.partial_ratio(x[0][col_one], x[1][col_one]) 
    >= fuzzy_threshold, combinations(object_one + object_two, 2)))
```
- Once the two Dataframes are merged, we import the merged table into PostgreSQL.
```python
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
```
### Utilizing Pandasai for Analysis
- **Pandasai**: Employed for data manipulation, exploration, and statistical analysis tailored to superhero video gaming data.
- Leveraging Pandasai features to delve into sales trends, user reviews, and correlations between various game attributes.

### Insights and Visualization - Streamlit
- Used combination of Streamlit and Pandasai to visualize the data and make some analysis.

```python
keys = json_reader("OPENAI_API")

df = postgres_data('merged_game_data')
# Centered Title
st.markdown("<h1 style='text-align:center'> SuperHero Video Game Analytics </h1>", unsafe_allow_html=True)

st.image('https://static1.colliderimages.com/wordpress/wp-content/uploads/2023/01/superman-logo-social-featured.jpg', caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

# Setup a script to get a prompt for an answer
prompt = st.text_input("Type in a question about the data: ")

# Setup pandasai
llm = OpenAI(api_token=keys)
pandasa = SmartDataframe(df, config={"llm": llm})

if st.button("Answer"):
    # Result 
    result = pandasa.chat(prompt)
    
    st.write(result)

    st.balloons()
```
![ezgif-7-26f53064b5](https://github.com/sinlesscoder/game-analytics/assets/121634275/b72e3f4b-9a41-48b4-b9e3-07b25453442b)
- Can ask any simple question regarding the data.
## Contents:
### Merging_tools.py 
 - In order to merge the two dataframe, we need to convert them into JSON by creating a method `create_json_from_df`. 

 ```python 
 # Turns a Dataframe into JSON
def create_json_from_df(df, cols):
    subset = df[cols]

    results = []

    for i in range(subset.shape[0]):
        row = subset.iloc[i]
        results.append(row.to_dict())
    
    return results
```
- A merging method `parse_combo_filer_df` is used to combine the two DataFrames. Since the foreign keys are similar but not exactly the same, we will need to use a module called `FuzzyWuzzy`. The module is a `Levenshtein Distance` tool that would give a percentage of how similar each value in the two foreign key columns are.

```python
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
```
- We only accept the two foreign value being the same if the FuzzyWuzzy result from the two is 90% or above. To use `combinations`, we need the data to be in a JSON format.
## Technologies Used

- **Python**: Core programming language utilized for data analysis and manipulation.
- **Pandasai**: Pandas-based library utilized for efficient analysis of superhero video gaming data.
- **Jupyter Notebooks**: Potentially used as the analysis environment for documentation and presentation of insights.
- **Visualization Libraries**: Matplotlib, Seaborn, or Plotly may be utilized for visual representation of analytical findings.

## Usage

To replicate and explore this project:
1. Ensure Python is installed along with necessary libraries including Pandasai.
2. Acquire or gather superhero video gaming data covering sales prices, release dates, game IDs, reviews, etc.
3. Follow the outlined data analysis process using Pandasai functionalities for exploration and manipulation.
4. Employ visualization tools to represent and interpret insights obtained from the analysis.

## Future Improvements

- Integration of machine learning models for predictive analysis or recommendation systems.
- Inclusion of additional datasets for more comprehensive analysis.
- Development of interactive dashboards for user-friendly presentation of insights.

## Contributors

- Ali Ahmed

Feel free to reach out with any questions or feedback!

