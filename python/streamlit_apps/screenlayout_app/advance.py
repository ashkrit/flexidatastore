import streamlit as st

st.set_page_config(page_title='Advance Page', page_icon=':robot_face:')
st.title("Page Configured")

st.success("Successful")
st.warning("Warning")
st.info("Info")
st.error("Error")
st.exception("It is an exception")


name = st.text_input('Text')
if not name:
  st.info('Enter any Text.')
  # Stop function
  st.stop()
st.success('Text Entered Successfully.')


sub_form = st.form(key='submit_form')
user_name = sub_form.text_input('Enter your username')
# Submit button associated with form
submit_button = sub_form.form_submit_button('Submit')
st.write('Press submit see username displayed below')
if submit_button:
    st.write(f'Hello!!!! {user_name}')


if 'sum' not in st.session_state:
    st.session_state.sum = 0
# Button to add value
add = st.button('Add One')
if add:
    st.session_state.sum += 1
st.write('Total Sum = ', st.session_state.sum)    