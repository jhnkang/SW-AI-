import streamlit as st
import random
import pandas as pd
import json
import firebase_admin
from firebase_admin import credentials, firestore

key_dict = json.loads(st.secrets["textkey"])
cred = credentials.Certificate(key_dict)


st.balloons()
st.markdown("<h1 style='font-size:50px;'>Hello, HI</h1>", unsafe_allow_html=True)

st.markdown('''
    :red[!] :orange[Find] :green[out] :blue[high-performance] :violet[electronic]
    :gray[devices]''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
# $ streamlit run test1.py

st.markdown("---")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Gas Price", "$4.00", "-$0.50", delta_color="inverse")
col5.metric("Active Developers", "123", "+10", delta_color="normal")

st.markdown("---")

df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

st.markdown("---")
st.link_button("Go to gallery", "https://streamlit.io/gallery")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
