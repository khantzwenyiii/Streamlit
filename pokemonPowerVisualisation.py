import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World! I will visualise the powes of 10 pokemon characters in this app!")

# loading dataset
pokemon = pd.read_csv("pokemon.csv")

# selecting only Name and Total columns of the first ten rows
first_10_characters = pokemon.loc[:10,["Name", "Total"]]


st.dataframe(first_10_characters)
st.bar_chart(data=first_10_characters, x="Name", y="Total")
