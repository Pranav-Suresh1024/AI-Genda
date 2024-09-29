import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key = "AIzaSyDw0SnHIWq68Z4_-31GyIvbZhsl_Pbfmjc")
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("FILE NOT FOUND!!")

st.set_page_config(page_title="Invoice Reader Website")
st.sidebar.header("Sidebar_Placeholder")
st.sidebar.write("Made by Pranav. Sample Text.")
st.header("INVOICE READER")
st.subheader("Subheader_Placeholder")
input_prompt = st.text_input("What do you want me to do?",key="input")
uploaded_file = st.file_uploader("Choose an image",type=["jpg","jpeg","png"])
image_var = ""
if uploaded_file is not None:
    image_var= Image.open(uploaded_file)
    st.image(image_var,caption="Uploaded Image",use_column_width=True)

sumbit_but = st.button("Sumbit Image")

ai_prompt = """
you are an expert in reading invoices. we are going to upload an image of an invoice an you will 
have to answer any type of questions that the user asks you.
you have to greet the user first. make sure to keep the fonts uniform and give the items list 
in a point wise format.
at the end, make sure to repeat the name of our app 'Invoice_Reader' and ask the user to use it 
again.
if image uplaoded is not an invoice display an error message to the user and also suggest them 
options on what they can do. """

if sumbit_but:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(ai_prompt,image_data,input_prompt)
    st.subheader("Here's what you need to know.")
    st.write(response)

