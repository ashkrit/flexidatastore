import streamlit as st
import pandas as pd
import time
import numpy as np

st.write("# USA Market Trends")

st.write("## SPY")
spy_df = pd.read_csv("../data/SPY_Data.csv")
st.line_chart(spy_df , x="Date", y="Price")

st.write("## QQQ")
qqq_df = pd.read_csv("../data/QQQ_Data.csv")
st.line_chart(qqq_df , x="Date", y="Open")


progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)
progress_bar.empty()

