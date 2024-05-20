"""Streamlit Definition of Server."""

import os

import streamlit as st
from dotenv import load_dotenv

from gimme_shelter.client import AvailableModels, produce_client
from gimme_shelter.prompt import prompt

# sidebar
with st.sidebar:
    selected_model = st.radio(
        "Select Model",
        options=AvailableModels,
        format_func=lambda x: x.value.display_name,
        captions=[model.value.provider for model in AvailableModels],
    )
    load_dotenv()
    client = produce_client(selected_model, secrets=os.environ)

# header
st.title("Gimme Shelter!")
st.caption(f"Model: {client.model.display_name}")
st.write(
    "Diese App schreibt dir, aus Wohnungsanzeigen,"
    " Anschreiben für den jeweiligen Vermieter.",
)

# input form
with st.form(key="input"):
    st.write("Gebe hier die Infos über die Wohnung ein.")
    input_anzeige = st.text_area(
        "Am besten Copy&Paste der Anzeige.",
        height=400,
    )
    is_submitted = st.form_submit_button("Generiere Anschreiben")

# generated text
if is_submitted:
    compiled_prompt = prompt(input_anzeige)
    response = client.request(compiled_prompt)
    st.markdown(response)
