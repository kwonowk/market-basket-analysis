import streamlit as st
import pandas as pd
import plotly.express as px



st.header('Which products are most commonly reordered by customers?')
st.divider()
order_num = st.slider("Number of top reordered products to display : ",
                      min_value = 30,
                      max_value = 100,
                      value = 30)

# Data format
data = pd.read_csv("reorders.csv")
data['reordered_percent'] = data['reordered_percent'].astype('object')
data.sort_values(by=['reordered'], ascending = False, inplace=True)
data_order = data[:order_num].sort_values(by='reordered')

# Display horizontal barchart
fig = px.bar(data_order,
             x=["reordered","ordered_once"],
             y="product_name",
             orientation= 'h',
             width = 1200, height = 1000)

# Manually add text annotations
for i, row in data_order.iterrows():
    fig.add_annotation(
        x=4000,
        y=row['product_name'],
        text=f"{int(row['reordered_percent'])} %",
        showarrow=False,
        xanchor='left',
        font=dict(
            color='white',
            size=14
        )
    )

fig.update_layout(
    xaxis_title="Number of total orders",
    yaxis_title="Product name",
    legend_title="Order type",
)

st.plotly_chart(fig)
