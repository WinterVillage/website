import streamlit as st
from helpers import file_helpers, image_helpers, streamlit_helpers
from pathlib import Path

script_dir = Path(__file__).parent.resolve()

resources_path = f"{script_dir.parent.parent}/resources/main/"

st.set_page_config(
    layout="centered"
)

# Initialize CSS of the page
st.markdown(
    f"<style>{file_helpers.read_file(f"{script_dir.parent.parent}/resources/main_style.css")}</style>",
    unsafe_allow_html=True
)

# Place the main logo as the entry
st.image(
    image_helpers.getCroppedImage(f"{script_dir.parent.parent}/resources/logo.png"),
    use_container_width=True
)

streamlit_helpers.customDivider()

# Place the welcome / entry text
streamlit_helpers.markdownByFile(
    file_path=resources_path + "text/welcome.md",
    width=0.8
)