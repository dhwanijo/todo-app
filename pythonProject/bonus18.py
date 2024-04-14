import streamlit as st
from PIL import Image

#st.set_page_config(layout="wide")

image_uploaded = st.file_uploader("Browse the image to upload:")

with st.expander("Start Camera"):
    # Open the Camera
    camera_image = st.camera_input("Camera")

# Create a Pillow instance of the image
if camera_image:
    image = Image.open(camera_image)

# Convert the image into gray
    gray_img = image.convert("L")

# Render the grayscale image on the webapp
    st.image(gray_img)

if image_uploaded:
    img = Image.open(image_uploaded)
    gray_upload = img.convert("L")
    st.image(gray_upload)