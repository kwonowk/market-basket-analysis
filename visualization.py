import streamlit as st
import pandas as pd
from pyvis import network as net
import networkx as nx

from stvis import pv_static


st.header('What are customers buying from our app?')
st.subheader('A Deepdive on Instacart Online Grocery Shopping Dataset')
st.title("")


with st.sidebar:
    st.title("")
    st.title("")
    st.title("")

    st.subheader("Purchase combinations")
    q1 = st.button("Which product groups are purchased together most frequently?")
    q2 = st.button("How do purchasing patterns for these product groups vary at different times of the day?")

    st.subheader("Purchase timing and frequency")
    q3 = st.button("What are the peak purchasing times during the week?")
    q4 = st.button("Which products are most commonly reordered by customers?")
    q5 = st.button("How frequently are products reordered on average?")
    q6 = st.button("What are the products that customers rarely or never reorder?")

    st.subheader("Purchase timing and frequency")
    q3 = st.button("Which products are typically bought as standalone items?")
    q4 = st.button("Are there products that are seldom or never purchased?")

data1  = pd.read_csv('q1-1.csv')
data2 = pd.read_csv('q1-2.csv')
data3 = pd.read_csv('q2-1.csv')
data4 = pd.read_csv('q2-2.csv')
data5 = pd.read_csv('q2-3.csv')

def network_graph(df):
        G = nx.from_pandas_edgelist(df, source='antecedent', target='consequent',
                                edge_attr='support_itemset_relative_pct')

        prod_net = net.Network(notebook = True, cdn_resources='in_line',
                            height="1000px",
                            width="1000px",
                            font_color="black")

        prod_net.barnes_hut()

        sources = df.antecedent
        targets = df.consequent
        weights = df.confidence_pct

        edge_data = zip(sources, targets, weights)

        for e in edge_data:
                        src = e[0]
                        dst = e[1]
                        w = e[2]

                        prod_net.add_node(src, src, title=src)
                        prod_net.add_node(dst, dst, title=dst)
                        prod_net.add_edge(src, dst, value=w)

        neighbor_map = prod_net.get_adj_list()

        nx.set_node_attributes(G,df.support_itemset_relative_pct*30,'size')

        # add neighbor data to node hover data
        for node in prod_net.nodes:
                        node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
                        node["value"] = len(neighbor_map[node["id"]])
                        node["font"] = {'size' : 100}

        pv_static(prod_net)

if q1:
    network_graph(data1)

if q2:
    if 'hour' not in st.session_state:
        st.session_state['hour'] = 0

    st.session_state.hour =  st.selectbox("Select hour: ",(range(0,24)))
    df = data2.loc[data2.hour == st.session_state.hour]
    st.dataframe(df)
