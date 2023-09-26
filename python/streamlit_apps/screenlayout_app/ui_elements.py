import streamlit as st
import time

st.title('Creating a Button')
# Defining a Button

counter=0

button = st.button('Click Here')
if button:
    counter = counter+1
    st.write('You have clicked the Button')
else:
     st.write('You have not clicked the Button')


gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

st.write('The value of the counter is', counter)


st.write('Select your Hobies:')
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')


# Creating Dropdown
hobby = st.selectbox('Choose your hobby: ',
        ('Books', 'Movies', 'Sports'))


hobbies = st.multiselect(
       'What are your Hobbies',
       ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
       ['Reading', 'Playing'])

download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')



with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')