import streamlit as st
import pandas as pd

# st.write("tire2")
tire4=pd.read_csv("tire4_final.csv")
tire4 = tire4.drop_duplicates()

tire4.fillna(0, inplace=True)


# Add a selectbox to the sidebar:
add_selectbox_state = st.sidebar.selectbox(
    'select the state',
    tire4['state_clean'].unique(),
)
add_selectbox_distrct = st.sidebar.selectbox(
    'district',
    tire4['district_clean'].unique())

# add_selectbox_year = st.sidebar.selectbox(
#     'year',
#     tire4['year'].unique())

state=tire4[tire4['state_clean']==add_selectbox_state]
#st.subheader("state")
# st.subheader(add_selectbox_state)

district=state[state["district_clean"]==add_selectbox_distrct]
#st.subheader("district")
# st.subheader(add_selectbox_distrct)

# year_n=district[district["district_clean"]==add_selectbox_year]
# # st.subheader("year")
# # st.write(add_selectbox_year)



state=state[["state_clean","district_clean","Risk","Risk_norm","year","Risk_Category"]]


# st.subheader("Graph")
# Line chart
#st.subheader(add_selectbox_district,"rainfall Trend")
# st.bar_chart(state,horizontal=False)
# st.write("### Risk Trends Per State")
# st.line_chart(tire4.set_index("state_clean")["Risk_norm"])

# st.subheader(add_selectbox_state)

# st.write("### Risk Trends per District")
# st.line_chart(state.set_index("district_clean")["Risk_norm"])

# # st.bar_chart(state.set_index("district_clean")["Risk_norm"])
# st.bar_chart(state, x="district_clean", y="Risk_Category",stack=True)




st.write("### Risk Trends Over Years per District")
# st.write(add_selectbox_state)
st.line_chart(
    state, 
    x="year", 
    y="Risk_norm", 
    color="district_clean"
)

# st.write("### Risk Trends Over Years per District")
# # st.write(add_selectbox_state)
# st.bar_chart(
#     state, 
#     x="year", 
#     y="Risk_Category", 
#     color="district_clean"
# )





