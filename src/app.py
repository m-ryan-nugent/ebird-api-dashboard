import streamlit as st

from src.data_fetcher import EBirdDataFetcher
from src.data_processor import EBirdDataProcessor
from src.visualizer import EBirdVisualizer
from src.text_formatter import TextFormatter
from src.constants import REGION_CODES


REGION_DICT = dict(REGION_CODES)

st.set_page_config(
    page_title="eBird API Dashboard",
    page_icon="🐦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("eBird API Dashboard")

api_col, openai_col, _ = st.columns(3)

with api_col:
    ebird_api_key = st.text_input(label="Enter EBird API Key:")

with openai_col:
    openai_api_key = st.text_input(
        label="Enter OpenAI API Key:", type="password"
    )

if ebird_api_key and openai_api_key:
    fetcher = EBirdDataFetcher(api_key=ebird_api_key)
    processor = EBirdDataProcessor()
    visualizer = EBirdVisualizer()
    formatter = TextFormatter(openai_api_key=openai_api_key)

    region_col, _, _ = st.columns(3)

    with region_col:
        selected_region = st.selectbox(
            "Select a Region",
            options=[code for code, _ in REGION_CODES],
            format_func=lambda x: f"{REGION_DICT[x]}",
        )
        fetch_data = st.button("Fetch and Analyze Data")

    if fetch_data:
        with st.spinner("Fetching recent observations..."):
            try:
                observations = fetcher.get_recent_observations(
                    region_code=selected_region
                )
            except Exception as e:
                st.error(f"Error getting observations: {e}")
                st.stop()

            df = processor.process_observations(observations=observations)
            top_ten = processor.top_ten_species(df=df)
            top_ten_plot = visualizer.plot_recent_observations(df=top_ten)

            st.header(f"Recent Observations in {REGION_DICT[selected_region]}")
            st.pyplot(top_ten_plot)

            st.header("Species Descriptions")
            species_list = top_ten.index.to_list()

            try:
                descriptions = formatter.get_species_descriptions(
                    species_list=species_list
                )
            except Exception as e:
                print(f"Error getting species descriptions: {e}")
                descriptions = None

            if descriptions:
                for species in species_list:
                    with st.expander(species):
                        st.write(descriptions[species])
            else:
                st.warning("Species descriptions could not be processed.")
