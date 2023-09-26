import streamlit as st
import datetime
import docx2txt
import pdfplumber

st.title("Text Box")
# Creating Text box with 10 as character limit
name = st.text_input("Enter your Name", max_chars=10)
st.write("Your Name is ", name)


password = st.text_input("Enter your password", type='password')
st.write("Your Pass is ", password)


# Creating Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered:  \n""",input_text)


value = st.number_input("Enter your Number")
st.write("Your Number is ", value)


num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0,  \n  Max. value is 10")
st.write("Default Value is 5,  \n  Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)


# Defining Time Function
st.time_input("Select Your Time")


st.date_input("Select Date")

st.date_input("Select Your Date", value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1))


input_file = st.file_uploader("Upload Document", type=["docx","pdf","txt","csv"])
details = st.button("Check Details")

if details:
    if input_file is not None:
        # Getting Document details like name, type and size
        doc_details = {"file_name":input_file.name, "file_type":input_file.type,
                        "file_size":input_file.size}
        st.write(doc_details)
        # Check for text/plain document type

        if input_file.type == "application/pdf":
            pdf = pdfplumber.open(input_file)
            pages = pdf.pages[0]
            st.write(pages.extract_text())
        elif input_file.type == "docx":
             # Read docx document type
            docx_text = docx2txt.process(input_file)
            st.write(docx_text)
        else:
            # Read document as string with utf-8 format
            raw_text = str(input_file.read(),"utf-8")
            st.write(raw_text)