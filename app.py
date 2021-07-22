import streamlit as st
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/pytesseract'
st.title("minor project")
img = st.file_uploader("chose an image")
if img is not None:
  img_read = Image.open(img)
  st.image(img)
  op = pytesseract.image_to_string(img_read)
  st.write(op)
