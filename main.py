import streamlit as st
import pandas as pd




main_page = st.Page("main.py", title="Main Page", icon="🎈")







# Define the pages
main_page = st.Page(r"main.py", title="Main Page", icon="🎈")
page_1 = st.Page(r"tire1.py", title="Discover Suraksha Lens with us", icon="❄️")

page_4 = st.Page(r"E:\suraksha_lens\dashboard\tire4.py", title="Climate Exploitation Risk Index (CERI)", icon="❄️")


# Set up navigation
pg = st.navigation([main_page,page_1,page_4])

# Run the selected page
pg.run()

