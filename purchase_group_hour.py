import pandas as pd
from pyvis import network as net
import streamlit as st
import networkx as nx
from stvis import pv_static

def network_graph(df):
        G = nx.from_pandas_edgelist(df, source='antecedent', target='consequent',
                                edge_attr='support_itemset_relative_pct')

        prod_net = net.Network(notebook = True, cdn_resources='in_line',
                            height="1000px",
                            width="1200px",
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

        # Add neighbor data to node hover data
        for node in prod_net.nodes:
                        node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
                        node["value"] = len(neighbor_map[node["id"]])
                        node["font"] = {'size' : 100}

        pv_static(prod_net)

st.header('How do purchasing patterns for these product groups vary at different times of the day?')
st.divider()

data  = pd.read_csv('purchase_group_hour.csv')
hour = st.slider("Select purchase hour to analyze : ", 0, 23)

if st.button("Show purchase groups"):
    data_hour = data.loc[data["hour"] == hour][:30]
    network_graph(data_hour)
