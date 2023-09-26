import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import graphviz as graphviz
import seaborn as sns


#Defining Columns
c1, c2, c3 = st.columns(3)
# Defining Metrics

c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")

st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")


df = pd.DataFrame(
     np.random.randn(30, 10),
     columns=('col_no %d' % i for i in range(10)))
# defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")


df = pd.DataFrame(
     np.random.randn(10, 2),
     columns=['a', 'b'])
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
     x='a', y='b',  tooltip=['a', 'b'])
# Defining Chart in write() function
st.write(chart)


s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
st.write(chart)


df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"])
# Bar Chart
st.bar_chart(df)


df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"])
st.line_chart(df)


df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"])
st.area_chart(df)


locate_map = pd.DataFrame(
  np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
  columns = ['latitude', 'longitude'])
# Map Function
st.map(locate_map)


st.graphviz_chart('''
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"
    }
''')