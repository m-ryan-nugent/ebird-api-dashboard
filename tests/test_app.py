import unittest
from unittest.mock import patch, MagicMock

from src.app import main
from src.data_fetcher import EBirdDataFetcher
from src.data_processor import EBirdDataProcessor
from src.visualizer import EBirdVisualizer
from src.text_formatter import TextFormatter


class TestApp(unittest.TestCase):

    @patch("streamlit.text_input")
    @patch("streamlit.selectbox")
    @patch("streamlit.button")
    @patch("streamlit.pyplot")
    @patch("streamlit.header")
    @patch("streamlit.write")
    @patch("streamlit.expander")
    def test_app_flow(
        self,
        mock_expander,
        mock_write,
        mock_header,
        mock_pyplot,
        mock_button,
        mock_selectbox,
        mock_text_input,
    ):
        mock_text_input.side_effect = [
            "fake_ebird_api_key",
            "fake_openai_api_key",
        ]
        mock_selectbox.return_value = "US-NY"
        mock_button.return_value = True
        mock_expander.return_value.__enter__.return_value = MagicMock()

        with patch.object(
            EBirdDataFetcher, "get_recent_observations"
        ) as mock_get_observations:
            mock_get_observations.return_value = [
                {"comName": "American Robin", "howMany": 5},
                {"comName": "Blue Jay", "howMany": 3},
            ]

            with patch.object(
                EBirdDataProcessor, "process_observations"
            ) as mock_process:
                mock_process.return_value = MagicMock()

                with patch.object(
                    EBirdVisualizer, "plot_recent_observations"
                ) as mock_plot:
                    mock_plot.return_value = MagicMock()

                    with patch.object(
                        TextFormatter, "get_species_descriptions"
                    ) as mock_descriptions:
                        mock_descriptions.return_value = {
                            "American Robin": "A common North American bird.",
                            "Blue Jay": "A colorful bird known for its intelligence.",
                        }

                        main()

        mock_get_observations.assert_called_once_with(region_code="US-NY")
        mock_process.assert_called_once()
        mock_plot.assert_called_once()
        mock_descriptions.assert_called_once()
        mock_pyplot.assert_called()
        mock_header.assert_called()


if __name__ == "__main__":
    unittest.main()
