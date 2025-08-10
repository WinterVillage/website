from pathlib import Path
import streamlit as st
from helpers import file_helpers, streamlit_helpers
import os

script_dir = Path(__file__).parent.resolve()
resources_path = f"{script_dir.parent.parent}/resources/guide/"

st.set_page_config(
    layout="centered"
)

# Initialize CSS of the page
st.markdown(
    f"<style>{file_helpers.read_file(f"{script_dir.parent.parent}/resources/main_style.css")}</style>",
    unsafe_allow_html=True
)

st.header("Guide", anchor=False)

streamlit_helpers.markdownByFile(
    file_path=resources_path + "text/explanation.md",
    width=0.8
)

streamlit_helpers.customDivider()

_, col, _ = st.columns([0.2, 0.6, 0.2])
with col:
    # Use ps.walk to iterate through all files in the 'resources_path + "guides"' directory
    for root, dirs, files in os.walk(resources_path + "guides"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with st.expander(label=file[:-3].upper(), expanded=False):
                    streamlit_helpers.markdownByFile(
                        file_path=file_path,
                        width=1.0
                    )