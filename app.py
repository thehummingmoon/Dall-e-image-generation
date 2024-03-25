from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey
from streamlit_carousel import carousel

client = OpenAI(api_key=apikey)

single_img=dict(
     title = "",
     text="",
     interval=None,
     img="",
)

def generate_images(image_description, num_images):
    image_gallery =[]
    for i in range(num_images):
        img_response =client.images.generate(
            model="dall-e-2",
            prompt=image_description,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = img_response.data[0].url
        new_image = single_img.copy()
        new_image["title"] =f"Image {i+1}"
        new_image["text"] =image_description
        new_image["img"] =image_url
        image_gallery.append(new_image)
    return image_gallery

st.set_page_config(page_title="Dalle-Image-Generation", page_icon=":camera:", layout="wide")

st.title("Dalle-Image-Generation Tool")

st.subheader("Powered By Dall-E")
img_description=st.text_input("Write your idea")
num_of_images=st.number_input("Number of images", min_value=1, max_value=5, value=1)

if st.button("Generate Images"):
    generate_image=generate_images(img_description,num_of_images)
    carousel(items=generate_image, width=1)
    