
import streamlit as st
import os
import tempfile
from core.predict import ImageClassifier
from PIL import Image

st.set_page_config(
    page_title="Image Classification App",
    page_icon="🧠",
    layout="centered"
)

cwd = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(cwd, "model", "cnn_model.pth")

@st.cache_resource
def load_classifier():
    return ImageClassifier(model_path=model_path, class_name=None)

classifier = load_classifier()

st.title("🧠 Image Classification App")
st.write("Upload an image to classify it as a Cat, Dog or Person.")

uploaded_file = st.file_uploader(
    "Upload your image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Classify Image", type="primary"):

        with tempfile.NamedTemporaryFile(
            suffix=".jpg",
            delete=False
        ) as temp_file:
            image_path = temp_file.name
            image.save(image_path, format="JPEG")

        try:
            with st.spinner("Classifying image..."):
                label, output_path = classifier.predict(image_path)

            st.success(f"Prediction: {label}")

            st.image(
                output_path,
                caption="Classified Image",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Prediction failed: {e}")

        finally:
            if os.path.exists(image_path):
                os.remove(image_path)
