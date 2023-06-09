import streamlit as st
import os
from PIL import Image
import io

def reduce_image(input_image_stream, size):
    original_image = Image.open(input_image_stream)
    width, height = original_image.size
    if width > height:
        max_size = (size, int((height / width) * size))
    else:
        max_size = (int((width / height) * size), size)

    original_image.thumbnail(max_size, Image.LANCZOS)
    output_image_stream = io.BytesIO()
    original_image.save(output_image_stream, format='JPEG', quality=90)
    output_image_stream.seek(0)
    return output_image_stream

st.title("Image Uploader")

# User input for file path
file_path = st.text_input('Enter your file path')

# Create an uploader
uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

# When a file is uploaded
if uploaded_file is not None and file_path:
    # Reduce the image size
    reduced_image_stream = reduce_image(uploaded_file, size=800)

    # Get the file
    file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
    st.write(file_details)

    # Save the reduced image to a new file on disk
    try:
        with open(os.path.join(file_path, uploaded_file.name), 'wb') as f:
            f.write(reduced_image_stream.read())
        st.success("Saved File:{} to {}".format(uploaded_file.name, file_path))
    except Exception as e:
        st.error(f"An error occurred: {e}")
