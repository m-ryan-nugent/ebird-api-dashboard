# eBird API Dashboard

This project is a Streamlit-based dashboard that fetches, processes, and visualizes bird observation data from the eBird API. It also provides species descriptions using OpenAI's models through the OpenAI API.

## Project Purpose

This project serves as a learning experience and skills demonstration. I understand that unit tests, github actions, and the overall structure of the project may be incorporating more advanced software development practices than might typically be applied to a simple web application. However, this approach allows for experimentation with various tools and methodologies, providing valuable learning opportunities and demonstrating a range of software development skills.

## Components

- `app.py`: Main Streamlit application that creates the dashboard interface
- `constants.py`: Contains project/wide constants (e.g., region codes and species codes)
- `data_fetcher.py`: Handles data retrieval from the eBird API
- `text_formatter.py`: Generates species descriptions using OpenAI's GPT-4o model
- `visualizer.py`: Creates visualizations of the processed bird observation data

## Getting started

1. Clone the repository
2. Create a virtual environment (optional but recommended):

```python
python -m venv .venv
source .venv/bin/activate # On Windows use `venv\Scripts\activate
```

3. Install required dependencies:

```python
pip install -r requirements.txt
```

4. Set up your eBird API key and OpenAI key
5. Run the Streamlit app:

```python
streamlit run src/app.py
```

## Usage

1. Enter your eBird API Key and OpenAI API key in the respective input fields
2. Select a region from the dropdown menu
3. Click "Fetch and Analyze Data" to retrieve and visualize recent bird observations
4. Explore the top 10 observed species chart and read their descriptions

## Testing

Unit tests are provided for each main component. To run tests:

```python
python -m unittest discover tests
```

## References

- eBird API 2.0: https://documenter.getpostman.com/view/664302/S1ENwy59
- OpenAI API Documentation: https://platform.openai.com/docs/overview
