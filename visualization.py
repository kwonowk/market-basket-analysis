import streamlit as st
def add_logo():
    st.markdown(
        """
<style>
    [data-testid="stSidebarNav"] {
        background-repeat: no-repeat;
        padding-top: 200px; /* Space above the content */
        position: relative;  /* Ensure the position is relative for absolute positioning of pseudo-elements */
    }
    [data-testid="stSidebarNav"]::before {
        content: "🔍 Deepdive on Instacart Online Grocery Shopping Dataset";  /* First block of text */
        color: black;       /* Set text color */
        font-size: 25px;    /* Set text size for the first block */
        font-weight: bold;
        line-height: 35px;
        position: absolute; /* Position absolutely within the relative parent */
        top: 50px;          /* Position from the top */
        left: 20px;         /* Position from the left */
    }
    [data-testid="stSidebarNav"]::after {
      content: ""; /* No text, used for the divider. */
        background: 	#C0C0C0; /* Divider color. */
        height: 1px; /* Height of the divider line. */
        width: 90%; /* Length of the divider line. */
        position: absolute; /* Positioned absolutely within the parent. */
        top: 180px; /* Positioned below the first text block. */
        left: 20px; /* Aligned with the left edge of the text block. */
    }
</style>
        """,
        unsafe_allow_html=True,
    )
add_logo()


# st.write("")


## Change to selectbar
pages = {
    "Purchase combinations":
    [
    st.Page("purchase_group_overall.py", title="Overall product purchase groups"),
    st.Page("purchase_group_hour.py", title="Hourly product purchase groups")
    ],

#     "Purchase timing and frequency" :
# [
#     st.Page(st.title(""), title = "Peak purchasing times during the week"),
#     st.Page(st.title(""), title = "Most commonly reordered products"),
#     st.Page(st.title(""), title = "Product reorder frequency"),
#     st.Page(st.title(""), title = "Never or seldomly reordered products")
#     ],

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
