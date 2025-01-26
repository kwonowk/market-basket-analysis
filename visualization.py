import streamlit as st
import pandas as pd
from pyvis import network as net
import networkx as nx
import streamlit.components.v1 as components
from stvis import pv_static



button_html = """
    <style>
        .btn {
            text-align: center;  /* Center the text */
            line-height: 50px;  /* Align text vertically */
            display: block;
            margin: 0 auto;  /* Center the button horizontally */
        }
    </style>
    <a href='#' class='btn'>Click me!</a>
"""


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
    pc100 = st.button('Test')

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
    G = nx.from_pandas_edgelist(data_1, source='antecedent', target='consequent',
                            edge_attr='support_itemset_relative_pct')

    got_net = net.Network(notebook = True, cdn_resources='in_line',
                        height="1000px",
                        width="1000px",
                        font_color="black")

    got_net.barnes_hut()

    sources = data_1.antecedent
    targets = data_1.consequent
    weights = data_1.confidence_pct

    edge_data = zip(sources, targets, weights)

    for e in edge_data:
                    src = e[0]
                    dst = e[1]
                    w = e[2]

                    got_net.add_node(src, src, title=src)
                    got_net.add_node(dst, dst, title=dst)
                    got_net.add_edge(src, dst, value=w)

    neighbor_map = got_net.get_adj_list()

    nx.set_node_attributes(G,data_1.support_itemset_relative_pct*10,'size')

    # add neighbor data to node hover data
    for node in got_net.nodes:
                    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
                    node["value"] = len(neighbor_map[node["id"]])
                    node["font"] = {'size' : 100}


    pv_static(got_net)

    HtmlFile = open("\\network_graph\product_network.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code, height = 500,width=800)

if pc2:
    st.write(data_2)


if pc100:
    pass
