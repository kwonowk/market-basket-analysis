import streamlit as st
import pandas as pd
import plotly.express as px

st.header('What are the products that customers never ordered?')
st.divider()

data = pd.read_csv('order_count.csv')
data = data[['product_id','product_name','count','aisle_id','department_id']]

st.dataframe(data, width = 1800, height = 440)
