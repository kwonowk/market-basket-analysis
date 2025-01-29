import streamlit as st
def add_logo():
    st.markdown(
        """
<style>
    [data-testid="stSidebarNav"] {
        background-repeat: no-repeat;
        padding-top: 200px;
        position: relative;
    }
    /*Display text*/
    [data-testid="stSidebarNav"]::before {
        content: "🔍 Deepdive on Instacart Online Grocery Shopping Dataset";
        color: black;
        font-size: 25px;
        font-weight: bold;
        line-height: 35px;
        position: absolute;
        top: 50px;
        left: 20px;
    }
    /*Define divider*/
    [data-testid="stSidebarNav"]::after {
      content: "";
        background: #C0C0C0;
        height: 1px;
        width: 100%;
        position: absolute;
        top: 180px;

    }
</style>
        """,
        unsafe_allow_html=True,
    )


add_logo()


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
    ]

#     "Individual product analysis":
#     [
#     st.Page(st.title(""), title = "Standalone purchases"),
#     st.Page(st.title(""), title = "Never or seldomly purchased products")
#     ]
}


# data2 = pd.read_csv('q1-2.csv')
# data3 = pd.read_csv('q2-1.csv')
# data4 = pd.read_csv('q2-2.csv')
# data5 = pd.read_csv('q2-3.csv')

pg=st.navigation(pages)
pg.run()

with st.sidebar:
    st.link_button("Who's dis?",
                   "https://www.notion.so/Insung-Kwon-172eee86853b80c2bc73c8493043fe84",
                   icon = "👀")
