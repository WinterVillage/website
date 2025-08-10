import os
from pathlib import Path
import streamlit as st
from helpers import file_helpers, streamlit_helpers
import requests

script_dir = Path(__file__).parent.resolve()
resources_path = f"{script_dir.parent.parent}/resources/application/"
appl_webhook_url = os.getenv("APPLICATION_DISCORD_WEBHOOK_URL")

def send_application():
    name = st.session_state.get("appl_input_name", "N/A")
    age = st.session_state.get("appl_input_age", "N/A")
    role = st.session_state.get("appl_input_role", "N/A")
    channel_link = st.session_state.get("appl_input_channel_link", "N/A")
    contact_method = st.session_state.get("appl_input_contact_method", "N/A")

    if contact_method == "Discord":
        contact_info = st.session_state.get("appl_input_discord", "N/A")
    else:
        contact_info = st.session_state.get("appl_input_email", "N/A")

    motivation = st.session_state.get("appl_input_motivation", "N/A")

    # Check if all required fields are filled (name & contact)
    if name == "N/A" or len(name) == 0 or contact_info == "N/A" or len(contact_info) == 0:
        st.session_state.appl_status = {
            "type": "error",
            "message": "Bitte fülle zumindest Kontakt-Infos & deinen Namen aus!"
        }
        return

    # Format the data into a message
    discord_message = f"""
**Winter Village Bewerbung**

---

**Name:** `{name}`
**Alter:** `{age}`
**Rolle:** `{role}`
**Kanal-Link:** `{channel_link}`

**Kontakt via:** `{contact_method}`
**Kontakt-Detail:** `{contact_info}`

---

**Motivation:**
```
{motivation}
```
"""

    data = {"content": discord_message}

    try:
        response = requests.post(appl_webhook_url, json=data)
        response.raise_for_status()

        # If the request was successful, update the session state with a success message
        st.session_state.appl_status = {
            "type": "success",
            "message": "Viele Dank für deine Bewerbung!"
        }
    except requests.exceptions.RequestException as e:
        st.session_state.appl_status = {
            "type": "error",
            "message": "Es gab einen Fehler beim versenden deiner Bewerbung!"
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
if "appl_status" not in st.session_state:
    st.session_state.appl_status = None

#st.title("Werde Teil von Winter Village!")
st.header("Werde Teil von Winter Village!", anchor=False)

streamlit_helpers.markdownByFile(
    file_path=resources_path + "text/explanation.md",
    width=0.8
)

streamlit_helpers.customDivider()

_, col, _ = st.columns([0.2, 0.6, 0.2])
with col:
    st.markdown("**Bewerbungsformular**")
    with st.container(border=True):
        st.markdown("**Wer bist du?**")
        with st.container(border=True):
            st.text_input("Name", placeholder="Dein Name ...", key="appl_input_name")
            st.number_input(
                "Alter",
                placeholder="Dein Alter ...",
                min_value=10,
                max_value=99,
                step=1,
                value=None,
                key="appl_input_age"
            )
            st.selectbox(
                "Für welche Rolle bewirbst du dich?",
                options=[
                    "Teilnehmer / Teilnehmerin",
                    "Content Creator"
                ],
                key="appl_input_role",
            )

            # If the user selects "Content Creator" show additional fields
            if st.session_state.get("appl_input_role") == "Content Creator":
                st.text_input("Kanal-Link", placeholder="Der Link zu deinem Kanal ...", key="appl_input_channel_link")

        st.markdown("**Wie kontaktieren wir dich?**")
        with st.container(border=True):
            st.selectbox(
                "Wie möchtest du kontaktiert werden?",
                options=[
                    "Discord",
                    "E-Mail"
                ],
                key="appl_input_contact_method"
            )

            if st.session_state.get("appl_input_contact_method") == "Discord":
                st.text_input("Discord", placeholder="Dein Discord-Tag ...", key="appl_input_discord")
            else:
                st.text_input("E-Mail", placeholder="Deine E-Mail-Adresse ...", key="appl_input_email")

        st.markdown("**Was ist deine Motivation?**")
        with st.container(border=True):
            st.text_area(
                "Warum möchstest du bei Winter Village mitmachen?",
                placeholder="Erzähl uns etwas über dich und deine Motivation ...",
                key="appl_input_motivation"
            )

        if st.session_state.appl_status:
            type = st.session_state.appl_status.get("type", "info")
            message = st.session_state.appl_status.get("message", "Keine Nachricht verfügbar.")

            if type == "success":
                st.success(message)
            elif type == "error":
                st.error(message)
            else:
                st.info(message)

        st.button(
            "Bewerbung abschicken",
            on_click=send_application,
            key="appl_send_application_button"
        )
