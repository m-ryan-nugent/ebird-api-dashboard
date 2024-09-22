from unittest import TestCase, main
from unittest.mock import patch

from src.data_fetcher import EBirdDataFetcher


class TestDataFetcher(TestCase):

    def setUp(self):
        self.api_key = "test_api_key"
        self.fetcher = EBirdDataFetcher(api_key=self.api_key)
        self.region_code = "US-NY"

    @patch("src.data_fetcher.requests.get")
    def test_get_recent_observations_success(self, mock_get):
        mock_response = [
            {
                "speciesCode": "amerob",
                "comName": "American Robin",
                "howMany": 5,
                "locName": "Test Location",
                "obsDt": "2023-09-01 08:00",
                "lat": 38.5,
                "lng": -121.6,
            }
        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        observations = self.fetcher.get_recent_observations(self.region_code)
        self.assertEqual(observations, mock_response)

    @patch("src.data_fetcher.requests.get")
    def test_get_recent_observations_failure(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {"error": "Invalid region"}

        observations = self.fetcher.get_recent_observations("Invalid-Region")
        self.assertIsNone(observations)


if __name__ == "__main__":
    main()
