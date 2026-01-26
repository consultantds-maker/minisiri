import streamlit as st
import pandas as pd

st.write("tire1")
# tire1=pd.read_csv("E:\suraksha_lens\data\TIER1_weekly_all_districts_1981_2025.csv")
# tire1=tire1[:10000]
# tire1

# option = st.selectbox(
#     'Which number do you like best?',
#      tire1['district'].unique())

# 'You selected: ', option

# rainfall=tire1[tire1["district"]==option]

# total_rainfall=rainfall["rainfall_mm"].sum()

# 'Total rainfall mm: ', total_rainfall
# rainfall

# st.line_chart(rainfall)
# import streamlit as stimport pandas as pdimport numpy as np
# st.title('mini_ceri')
"""My first appHere's our first attempt at using data to create a table:"""


# chart_data = pd.DataFrame(#      np.random.randn(20, 3),#      columns=['a', 'b', 'c'])
# st.line_chart(chart_data)


df = pd.read_csv("E:\suraksha_lens\data\TIER1_weekly_all_districts_1981_2025.csv")
df=df[:10000]
df

# Add a selectbox to the sidebar:
add_selectbox_district = st.sidebar.selectbox(
    'select the district',
    df['district'].unique(),
)
add_selectbox_week_start = st.sidebar.selectbox(
    'week_start period',
    df['week_start'].unique())

selected_date = st.sidebar.slider("Select rainfall",
df['rainfall_mm'].min(),
df['rainfall_mm'].max()
)
st.subheader(add_selectbox_district)

rainfall=df[df['district']==add_selectbox_district]
total_rainfall=str(rainfall['rainfall_mm'].sum())
st.subheader("Rainfall in MM")
st.write(total_rainfall)
#add_selectbox_district,' Data', df[df['district']==add_selectbox_district]
filtered_df=df[df['district']==add_selectbox_district]
# Line chart
#st.subheader(add_selectbox_district,"rainfall Trend")
st.line_chart(filtered_df.set_index("week_start")["rainfall_mm"])

