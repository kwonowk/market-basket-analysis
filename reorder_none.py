import streamlit as st
import pandas as pd
import plotly.express as px

st.header('What are the products that customers rarely or never reorder?')
st.divider()



data = pd.read_csv('purchase_frequency.csv').sort_values(by = 'days', ascending = False)[:60].sort_values(by='days')

# Display horizontal barchart
fig = px.bar(data,
             x="days",
             y="product_name",
             orientation= 'h',
             width = 1200, height = 1000)

fig.update_layout(
    xaxis_title="Average days between reorders",
    yaxis_title="Product name",
    legend_title="Order type",
)

st.plotly_chart(fig)
