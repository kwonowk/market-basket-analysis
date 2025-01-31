import streamlit as st
import pandas as pd
import plotly.express as px

st.header('How frequently are products reordered on average?')
st.divider()

data = pd.read_csv('purchase_frequency.csv').sort_values(by = 'days')[:60].sort_values(by='days', ascending = False)

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
