"""Streamlit Definition of Server."""

import streamlit as st

from gimme_shelter.request import AARequester

aa_requester = AARequester()


st.title("Gimme Shelter!", divider="rainbow")
st.write(
    "Diese App schreibt dir, aus Wohnungsanzeigen,"
    " Anschreiben fuer den jeweiligen Vermieter.",
)

with st.form(key="input"):
    st.write("Gebe hier die Infos ueber die Wohnung ein.")
    input_anzeige = st.text_area(
        "Am besten Copy&Paste der Anzeige.",
    )
    is_submitted = st.form_submit_button("Generiere Anschreiben", on_click=aa_requester)


if is_submitted:
    while response := aa_requester.response is None:
        st.spinner("Generiere Anschreiben")

    st.text(response)
