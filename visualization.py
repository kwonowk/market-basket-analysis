import streamlit as st


st.header('What are customers buying from our app?')
st.write('🔍 Deepdive on Instacart Online Grocery Shopping Dataset')
st.divider()
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
