import streamlit as st
import google.generativeai as genai
from PIL import Image

# API Key
GOOGLE_API_KEY = "AIzaSyD-rdl0rLz71HEAqc_kX9QsBrWSyfVbUt4"
genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="AI Cyber Eye", layout="centered")

st.title("👁️ AI සයිබර් ඇස")
st.write("මම ඔයාගේ AI සහායකයා. මට පින්තූරයක් දෙන්න, මම ඒක විස්තර කරන්නම්.")

mode = st.selectbox("මොනවාද කරන්න ඕනේ?", 
                   ["වටපිටාව අඳුනාගැනීම", "මුදල් සහ බිල්පත් කියවීම", "මුහුණේ ස්වභාවය බැලීම", "පොත් සහ ලේඛන කියවීම"])

img_file = st.camera_input("පින්තූරයක් ගන්න (Take Photo)")

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="පින්තූරය ලැබුණා", use_column_width=True)
    
    if mode == "වටපිටාව අඳුනාගැනීම":
        prompt = "Describe this environment in detail for a visually impaired person in Sinhala. Mention obstacles and objects."
    elif mode == "මුදල් සහ බිල්පත් කියවීම":
        prompt = "Identify any currency notes or bills in this image. Tell the value and details in Sinhala."
    elif mode == "මුහුණේ ස්වභාවය බැලීම":
        prompt = "Identify the person's facial expression and mood in this image. Explain it in Sinhala."
    else:
        prompt = "Read the text in this image (from a book or document) and provide the summary in Sinhala."

    model = genai.GenerativeModel('gemini-1.5-flash')
    
    with st.spinner("මම පින්තූරය පරීක්ෂා කරනවා..."):
        response = model.generate_content([prompt, img])
        st.subheader("පිළිතුර:")
        st.write(response.text)
        st.info("Talkback මගින් ඉහත පිළිතුර කියවනු ඇත.")
