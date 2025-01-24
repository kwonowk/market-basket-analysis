import streamlit as st
import pandas as pd

st.header('What are customers buying from our app?')
st.subheader('A Deepdive on Instacart Online Grocery Shopping Dataset')
st.title("")


with st.sidebar:
    st.title("")
    st.title("")
    st.title("")
    st.subheader("Purchase combinations")
    pc1 = st.button("Which product groups are purchased together most frequently?")

    pc2 = st.button("How do purchasing patterns for these product groups vary at different times of the day?")

# How do purchasing patterns for these product groups vary at different times of the day?
# Purchase timing and frequency

# What are the peak purchasing times during the week?
# Which products are most commonly reordered by customers?
# How frequently are products reordered on average?
# Individual product analysis

# Which products are typically bought as standalone items?
# What are the products that customers rarely or never reorder?
# Are there products that are seldom or never purchased?")
import pandas as pd

data_1  = pd.read_csv('q1-1.csv')
data_2 = pd.read_csv('q1-2.csv')

if pc1:
    st.write(data_1)

if pc2:
    st.write(data_2)
