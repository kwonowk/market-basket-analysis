import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Which products are typically bought as standalone items?')
st.divider()


data = pd.read_csv('transactions_single.csv')
data.columns = ['product_name','order_count']

order_num = st.slider("Number of top single purchase products to display : ",
                      min_value = 30,
                      max_value = 100,
                      value = 30)

data_ordered = data[:order_num].sort_values(by = 'order_count')

# Display horizontal barchart
fig = px.bar(data_ordered,
             x="order_count",
             y="product_name",
             orientation = 'h',
             width = 1200, height = 1000)

fig.update_layout(
    xaxis_title="Average days between orders",
    yaxis_title="Product name",
    legend_title="Order type",
)

st.plotly_chart(fig)
