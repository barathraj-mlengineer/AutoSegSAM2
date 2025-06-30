import streamlit as st
from PIL import Image
from main import run_pipeline

# Page config
st.set_page_config(page_title="🎭 Face & Hand Segmentor", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🧠 AI Segmentor")
    st.markdown(
        """
        Upload an image and this app will detect and highlight **faces** and **hands** using MediaPipe.

        - Works with JPG, PNG
        - Results shown side-by-side
        """
    )
    st.info("Built with ❤️ using Streamlit & MediaPipe")

# Main Title
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>🎭 Face & Hand Segmentation App</h1>", unsafe_allow_html=True)
st.markdown("---")

# File uploader
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    # Layout with columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📸 Original Image")
        st.image(image, use_column_width=True)

    with st.spinner("🔍 Processing Image..."):
        output = run_pipeline(image)

    with col2:
        st.subheader("🎯 Segmented Output")
        st.image(output, use_column_width=True)

    st.success("✅ Segmentation Complete!")
else:
    st.markdown(
        "<div style='text-align: center; color: gray;'>Please upload an image file from the sidebar to begin.</div>",
        unsafe_allow_html=True
    )
