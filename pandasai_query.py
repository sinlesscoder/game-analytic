import streamlit as st
from json import load
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from os import getcwd
from json_read import json_reader
from postgres_conn import postgres_data

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
