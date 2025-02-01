import streamlit as st
st.set_page_config(page_title = "Market Basket Analysis", layout = "wide")

def add_sidebar_text():
    st.markdown(
        """
<style>
    /*Modify side bar*/
    [data-testid="stSidebarNav"] {
        background-repeat: no-repeat;
        padding-top: 160px;
        position: relative;
    }
    /*Display title text at the top of the side bar*/
    [data-testid="stSidebarNav"]::before {
        content: "🔍 Deepdive on Instacart Online Grocery Shopping Dataset";
        color: black;
        font-size: 25px;
        font-weight: bold;
        line-height: 35px;
        position: absolute;
        top: 10px;
        left: 20px;
    }
    /*Define divider below title text*/
    [data-testid="stSidebarNav"]::after {
      content: "";
        background: #C0C0C0;
        height: 1px;
        width: 100%;
        position: absolute;
        top: 138px;
    }

    /*Make page wider*/
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
        width: 400px;
        margin-left: -400px;
    }

</style>
        """,
        unsafe_allow_html=True,
    )

add_sidebar_text()

pages = {
    "About the project" :
    [st.Page('about.py', title = "Project overview")],
    "Purchase combinations":
    [
    st.Page("purchase_group_overall.py", title="Overall product purchase groups"),
    st.Page("purchase_group_hour.py", title="Hourly product purchase groups")
    ],

    "Purchase timing and frequency" :
[
    st.Page("purchase_time.py", title = "Peak purchasing times during the week"),
    st.Page("reorder_product.py", title = "Most commonly reordered products"),
    st.Page("reorder_frequency.py", title = "Product reorder frequency"),
    st.Page("reorder_none.py", title = "Never or seldomly reordered products")
    ],

    "Individual product analysis":
    [
    st.Page("transactions_single.py", title = "Standalone purchases"),
    st.Page("order_count.py", title = "Never ordered products")
    ]
}

pg=st.navigation(pages)
pg.run()

with st.sidebar:
    st.link_button("Who's dis?",
                   "https://www.notion.so/Insung-Kwon-172eee86853b80c2bc73c8493043fe84",
                   icon = "👀")
