import streamlit as st
from helpers import image_helpers
from pathlib import Path

script_dir = Path(__file__).parent.resolve()

# Define the pages
main_page = st.Page(str(script_dir) + "/pages/main_page.py", title="Home", icon="❄️")
application_page = st.Page(str(script_dir) + "/pages/application.py", title="Bewerbung", icon="🫱")
contact_page = st.Page(str(script_dir) + "/pages/contact.py", title="Kontakt", icon="📧")
guide_page = st.Page(str(script_dir) + "/pages/guide.py", title="Guide", icon="💡")

# Set up navigation
pg = st.navigation(
    {
        "Home": [main_page],
        "Kontakt": [application_page, contact_page],
        "Guide": [guide_page],
    }
)

# Set a logo (for the navigation bar)
st.logo(image_helpers.getCroppedImage(
    image_path=f"{script_dir.parent}/resources/logo.png"
))

# Run the selected page
pg.run()