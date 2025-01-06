import streamlit as st
import numpy as np
from rembg import remove
from PIL import Image
import io

# Function to remove background
def remove_background(image):
    # Convert the image to a numpy array
    image_np = np.array(image)
    # Remove the background
    output_image = remove(image_np)
    return output_image

# Streamlit app
st.title("Image Background Remover by Vatsa")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    
    # Display the original image
    st.image(image, caption='Original Image', use_container_width=True)

    # Remove background
    output_image = remove_background(image)

    # Convert output image to PIL format for display
    output_image_pil = Image.fromarray(output_image)

    # Display the output image
    st.image(output_image_pil, caption='Image with Background Removed', use_container_width=True)

    # Convert the output image to bytes for download
    buffered = io.BytesIO()
    output_image_pil.save(buffered, format="PNG")
    img_str = buffered.getvalue()

    # Download button
    st.download_button(
        label="Download Image",
        data=img_str,
        file_name="output_image.png",
        mime="image/png"
    )
