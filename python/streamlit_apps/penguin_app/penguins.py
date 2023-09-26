import streamlit as st
import pandas as pd

import altair as alt


st.title("Palmer's Penguins")

st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')


#selected_species = st.selectbox('What species would you like to visualize?',['Adelie', 'Gentoo', 'Chinstrap'])

selected_x_var = st.selectbox('What do want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_gender = st.selectbox('What gender do you want to filter for?',
                               ['all penguins', 'male penguins', 'female penguins'])

penguin_file = st.file_uploader("Select Your Local Penguins CSV (default provided)")

@st.cache_data
def load_data(file):
    print("Loading data")
    if file is not None:
        return pd.read_csv(file)
    else:
        return pd.read_csv('../../data/penguins.csv')

penguins_df= load_data(penguin_file)

#st.stop() ## This allow to do flow control

# import our data
st.write(penguins_df.head())

if selected_gender=='male penguins':
    penguins_df = penguins_df[penguins_df["sex"]=='male']
elif selected_gender=='female penguins':    
     penguins_df = penguins_df[penguins_df["sex"]=='female']
else:
    pass     


#penguins_df = penguins_df[penguins_df['species'] == selected_species]
alt_chart = (
    alt.Chart(penguins_df, title=f"Scatterplot of {selected_gender} Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species"
    )
    .interactive()
)
st.altair_chart(alt_chart,use_container_width=True)
