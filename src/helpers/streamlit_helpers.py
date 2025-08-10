import streamlit as st
from helpers import file_helpers

def customDivider(width: float = 0.5) -> None:
    """
    Places a custom divider in the Streamlit app layout.

    Args:
        width (float): The width of the divider as a fraction of the parent container width. Default is 0.5.

    Returns:
        None
    """
    _, main, _ = st.columns([(1-width)/2, width, (1- width)/2])
    with main:
        c1, c2, c3 = st.columns([6, 1, 6])
        with c1:
            st.markdown("---")

        with c2:
            st.markdown("")
            st.markdown("❆")

        with c3:
            st.markdown("---")

def markdownByFile(file_path: str, width: float = 1.0):
    """
    Places a markdown file in the Streamlit app layout.

    Args:
        file_path (str): The path to the markdown file.
        width (float): The width of the markdown content as a fraction of the parent container width. Default is 1.0.

    Returns:
        None
    """
    if width < 0.0 or width > 1.0:
        raise ValueError("Width must be between 0.0 and 1.0")

    file_content = file_helpers.read_file(file_path)

    if width == 1.0:
        st.markdown(file_content)
        return

    if file_content:
        _, main, _ = st.columns([(1-width)/2, width, (1- width)/2])
        with main:
            st.markdown(file_content)