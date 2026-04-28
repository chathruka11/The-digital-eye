import streamlit as st
import google.generativeai as genai
from PIL import Image

# API Key
GOOGLE_API_KEY = "AIzaSyD-rdl0rLz71HEAqc_kX9QsBrWSyfVbUt4"

# Gemini සම්බන්ධ කිරීම (නව මොඩල් නාමය සහිතව)
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    # මෙතන නම 'models/gemini-1.5-flash-latest' ලෙස වෙනස් කළා
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"සම්බන්ධතාවයේ දෝෂයක්: {e}")

st.set_page_config(page_title="AI Cyber Eye", layout="centered")

st.title("👁️ AI සයිබර් ඇස")
st.write("පින්තූරයක් ලබා දී විස්තර ලබාගන්න.")

mode = st.selectbox("තෝරන්න:", 
                   ["වටපිටාව අඳුනාගැනීම", "මුදල් සහ බිල්පත්", "මුහුණේ ස්වභාවය", "පොත් සහ ලේඛන"])

img_file = st.camera_input("පින්තූරයක් ගන්න")

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="පින්තූරය ලැබුණා", use_column_width=True)
    
    if mode == "වටපිටාව අඳුනාගැනීම":
        prompt = "Describe this environment in detail for a visually impaired person in Sinhala."
    elif mode == "මුදල් සහ බිල්පත්":
        prompt = "Identify any currency notes or bills in this image in Sinhala."
    elif mode == "මුහුණේ ස්වභාවය":
        prompt = "Describe the person's mood and expression in Sinhala."
    else:
        prompt = "Read the text in this image and summarize in Sinhala."

    try:
        with st.spinner("පරීක්ෂා කරමින් පවතිී..."):
            response = model.generate_content([prompt, img])
            st.subheader("පිළිතුර:")
            st.write(response.text)
    except Exception as e:
        st.error(f"ඇත්තම දෝෂය (Error): {e}")
