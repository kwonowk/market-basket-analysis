import streamlit as st
import altair as alt
import pandas as pd
import plotly.graph_objects as go

st.header('What are the peak purchasing times during the week?')
st.divider()

data = pd.read_csv('order_grouped.csv').rename({'order_dow': 'Day of Week',
                                                'order_hour_of_day' : 'hour'}, axis = 1)

data['Day of Week'] = data['Day of Week'].apply(lambda x: "DoW " + str(x))


chart = alt.Chart(data).mark_bar().encode(
    x='hour:O',
    y='count:Q',
    column='Day of Week:O',
    color=alt.Color('count:Q')
).properties(
    width=130,
    height=400,
)


st.altair_chart(chart)
