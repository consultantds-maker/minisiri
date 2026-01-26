import streamlit as st
import pandas as pd

st.write("tire2")
tire2=pd.read_csv("E:\suraksha_lens\data\TIER2_annual_1981_2025.csv")
tire2


# Add a selectbox to the sidebar:
add_selectbox_district = st.sidebar.selectbox(
    'select the district',
    tire2['district'].unique(),
)
add_selectbox_year = st.sidebar.selectbox(
    'year',
    tire2['year'].unique())

selected_date = st.sidebar.slider("Select population",
tire2['population'].min(),
tire2['population'].max()
)

st.subheader(add_selectbox_district)

st.subheader("year")
st.write(add_selectbox_year)

population=tire2[tire2['district']==add_selectbox_district]

population_per_year=population[population["year"]==add_selectbox_year]


total_population=str(population_per_year['population'].sum())
st.subheader("total_population")
st.write(total_population)





#add_selectbox_district,' Data', df[df['district']==add_selectbox_district]
filtered_df=tire2[tire2['district']==add_selectbox_district]

st.subheader("Filetred data frame")
population_per_year


st.subheader("Graph")
# Line chart
#st.subheader(add_selectbox_district,"rainfall Trend")
st.line_chart(filtered_df.set_index("year")["population"])

