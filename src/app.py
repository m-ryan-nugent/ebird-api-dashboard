import os
import sys

import streamlit as st

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.data_fetcher import EBirdDataFetcher
from src.data_processor import EBirdDataProcessor
from src.visualizer import EBirdVisualizer
from src.text_formatter import TextFormatter
from src.constants import REGION_CODES


REGION_DICT = dict(REGION_CODES)

st.set_page_config(layout="wide")
st.title("EBird API Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    api_key = st.text_input(label="Enter EBird API Key:")

if api_key:
    fetcher = EBirdDataFetcher(api_key=api_key)
    processor = EBirdDataProcessor()
    visualizer = EBirdVisualizer()
    formatter = TextFormatter()

    tab1, tab2, tab3 = st.tabs(["Recent Observations", "Tab 2", "Tab 3"])

    with tab1:
        col1, col2, col3 = st.columns(3)

        with col1:
            selected_region = st.selectbox(
                "Select a Region",
                options=[code for code, _ in REGION_CODES],
                format_func=lambda x: f"{REGION_DICT[x]}",
            )
            button = st.button("Fetch and Analyze Data")

        col1, col2 = st.columns(2)

        with col1:
            if button:
                with st.spinner("Fetching recent observations..."):
                    observations = fetcher.get_recent_observations(
                        region_code=selected_region
                    )
                    df = processor.process_observations(
                        observations=observations
                    )
                    top_ten_df = processor.top_ten_species(df=df)

                    top_ten_plot = visualizer.plot_recent_observations(
                        df=top_ten_df,
                    )
                    st.header(
                        "Recent Observations in"
                        f" {REGION_DICT[selected_region]}"
                    )
                    st.pyplot(top_ten_plot)

        with col2:
            if button:
                st.header("Species Descriptions")
                formatter.format_species_description(top_ten_df)

else:
    st.warning("Please enter your EBird API key to continue")
