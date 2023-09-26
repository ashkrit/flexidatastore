import streamlit as st
import pandas as pd

st.write("# USA Market Trends")

st.write("## SPY")
spy_df = pd.read_csv("../data/SPY_Data.csv")
st.line_chart(spy_df , x="Date", y="Price")

st.write("## QQQ")
qqq_df = pd.read_csv("../data/QQQ_Data.csv")
st.line_chart(qqq_df , x="Date", y="Open")
