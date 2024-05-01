"""Streamlit Definition of Server."""

import streamlit as st

from gimme_shelter.client import produce_client
from gimme_shelter.prompt import prompt

options = "AlephAlpha-Luminous"

# sidebar
with st.sidebar:
    model_selection = st.radio("Select Model", options=options)
    # TODO(Max): make radio and captions based on Enums

    model_client = produce_client(model_selection)


st.title("Gimme Shelter!", divider="rainbow")
st.caption(f"Model: {model_selection}")
st.write(
    "Diese App schreibt dir, aus Wohnungsanzeigen,"
    " Anschreiben für den jeweiligen Vermieter.",
)

with st.form(key="input"):
    st.write("Gebe hier die Infos ueber die Wohnung ein.")
    input_anzeige = st.text_area(
        "Am besten Copy&Paste der Anzeige.",
    )
    is_submitted = st.form_submit_button("Generiere Anschreiben")


if is_submitted:
    compiled_prompt = prompt()
    response = model_client.request(compiled_prompt)
    st.text(response)
