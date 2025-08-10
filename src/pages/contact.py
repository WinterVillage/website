import os
from pathlib import Path
import streamlit as st
from helpers import file_helpers
import requests

script_dir = Path(__file__).parent.resolve()
resources_path = f"{script_dir.parent.parent}/resources/contact/"
contact_webhook_url = os.getenv("CONTACT_DISCORD_WEBHOOK_URL")

def send_message():
    name = st.session_state.get("contact_input_name", None)
    email = st.session_state.get("contact_input_email", None)
    message = st.session_state.get("contact_input_message", None)

    # Check if everything is filled out
    if not name or len(name) == 0 or not email or len(email) == 0 or not message or len(message) == 0:
        st.session_state.status = {
            "type": "error",
            "message": "Bitte fülle alle Felder aus!"
        }
        return

    # Format the data into a message
    discord_message = f"""
**Neuer Kontaktformular-Eintrag**

---

**Name:** `{name}`
**E-Mail:** `{email}`

**Nachricht:**
```
{message}
```
"""

    data = {"content": discord_message}

    try:
        response = requests.post(contact_webhook_url, json=data)
        response.raise_for_status()

        # If the request was successful, update the session state with a success message
        st.session_state.contact_status = {
            "type": "success",
            "message": "Vielen Dank für deine Nachricht! Wir werden uns bald bei dir melden."
        }
    except requests.exceptions.RequestException as e:
        # If there was an error, update the session state with an error message
        st.session_state.contact_status = {
            "type": "error",
            "message": f"Es gab ein Problem beim Senden deiner Nachricht: {str(e)}"
        }

st.set_page_config(
    layout="centered"
)

# Initialize CSS of the page
st.markdown(
    f"<style>{file_helpers.read_file(f"{script_dir.parent.parent}/resources/main_style.css")}</style>",
    unsafe_allow_html=True
)

# Initialize session state variables
if "contact_status" not in st.session_state:
    st.session_state.contact_status = None

st.header("**Kontakt**", anchor=False)

st.markdown("**Kontaktformular**")
_, col, _ = st.columns([0.2, 0.6, 0.2])
with col:
    with st.container(border=True):
        st.text_input(
            "Name",
            placeholder="Dein Name ...",
            key="contact_input_name"
        )

        st.text_input(
            "E-Mail",
            placeholder="Deine E-Mail-Adresse ...",
            key="contact_input_email"
        )

        st.text_area(
            "Nachricht",
            placeholder="Deine Nachricht ...",
            key="contact_input_message"
        )

        if st.session_state.contact_status:
            type = st.session_state.contact_status.get("type", "info")
            message = st.session_state.contact_status.get("message", "Keine Nachricht")
            if type == "success":
                st.success(message)
            elif type == "error":
                st.error(message)
            else:
                st.info(message)

        st.button(
            "Absenden",
            on_click=send_message,
            key="contact_send_message_button"
        )
