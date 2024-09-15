import streamlit as st


class TextFormatter:
    def __init__(self):
        pass

    def format_species_description(self, series):
        for idx, val in series.items():
            st.markdown(f"{idx} - Description\n")
