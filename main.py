import streamlit as st
import pandas as pd



import streamlit as st



# Define the pages
main_page = st.Page("main.py", title="Main Page", icon="🎈")
page_1 = st.Page(r"tire1.py", title="Tire 1", icon="❄️")
page_2 = st.Page(r"tire2.py", title="Tire 2", icon="❄️")
page_3 = st.Page(r"E:\suraksha_lens\dashboard\tire3.py", title="Tire 3", icon="❄️")
page_4 = st.Page(r"E:\suraksha_lens\dashboard\tire4.py", title="Tire 4", icon="❄️")

# Set up navigation
pg = st.navigation([main_page,page_1, page_2, page_3,page_4])

# Run the selected page

pg.run()
