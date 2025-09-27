import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import io
import pickle
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input

# Set custom web page title
st.set_page_config(page_title="Caption Generator App", page_icon="📷")

# Streamlit app
st.title("Image Caption Generator")
st.markdown(
    "Upload an image, and this app will generate a caption for it."
)

@st.cache_resource
def load_legacy_components():
    # Load MobileNetV2 model
    mobilenet_model = MobileNetV2(weights="imagenet")
    mobilenet_model = Model(inputs=mobilenet_model.inputs, outputs=mobilenet_model.layers[-2].output)

    # Load your trained model
    model = tf.keras.models.load_model('mymodel.h5')

    # Load the tokenizer
    with open('tokenizer.pkl', 'rb') as tokenizer_file:
        tokenizer = pickle.load(tokenizer_file)

    return mobilenet_model, model, tokenizer

# Initialize legacy components (not used for inference but present per requirement)
legacy_mobilenet, legacy_model, legacy_tokenizer = load_legacy_components()

@st.cache_resource
def load_blip():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def describe_image(image_bytes: bytes) -> str:
    processor, model = load_blip()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=30)
    description = processor.decode(out[0], skip_special_tokens=True)
    return description

# Upload image
uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Process uploaded image
if uploaded_image is not None:
    image_bytes = uploaded_image.read()
    image_pil = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    st.subheader("Uploaded Image")
    st.image(image_pil, caption="Uploaded Image", use_column_width=True)

    st.subheader("Generated Caption")
    with st.spinner("Generating caption..."):
        generated_caption = describe_image(image_bytes)

    # Display the generated caption with custom styling
    st.markdown(
        f'<div style="border-left: 6px solid #ccc; padding: 5px 20px; margin-top: 20px;">'
        f'<p style="font-style: italic;">“{generated_caption}”</p>'
        f'</div>',
        unsafe_allow_html=True
    )