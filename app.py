

import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
from PIL import Image
import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#load Gemini Pro Vision


def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text 

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title = "Multilanguage PDF Extractro")
st.header("Gemini Application")
input = st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an file...", type=['jpg','jpeg','png'])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width =True)

submit = st.button("Tell me about file")
input_prompt = """
You are an expert in understanding report file. We will upload a image as report of a hotel
and you will have to answer any question based on the uploaded report file
"""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is")
    st.write(response)

