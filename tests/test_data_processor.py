from unittest import TestCase, main

import pandas as pd

from src.data_processor import EBirdDataProcessor


class TestDataProcessor(TestCase):

    def setUp(self):
        self.processor = EBirdDataProcessor()
        self.observations = [
            {
                "speciesCode": "amerob",
                "comName": "American Robin",
                "howMany": 5,
                "locName": "Location A",
                "obsDt": "2023-09-01 08:00",
                "lat": 38.5,
                "lng": -121.5,
            },
            {
                "speciesCode": "houspa",
                "comName": "House Sparrow",
                "howMany": 3,
                "locName": "Location B",
                "obsDt": "2023-09-02 09:30",
                "lat": 38.6,
                "lng": -121.6,
            },
            {
                "speciesCode": "amerob",
                "comName": "American Robin",
                "howMany": 2,
                "locName": "Location C",
                "obsDt": "2023-09-03 07:15",
                "lat": 38.7,
                "lng": -121.7,
            },
        ]

    def test_process_observations(self):
        df = self.processor.process_observations(self.observations)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("month", df.columns)
        self.assertIn("year", df.columns)
        self.assertEqual(len(df), 3)

    def test_top_ten_species(self):
        df = self.processor.process_observations(self.observations)
        top_ten = self.processor.top_ten_species(df)

        self.assertEqual(len(top_ten), 2)
        self.assertEqual(top_ten.index[0], "American Robin")
        self.assertEqual(top_ten.iloc[0], 7)


if __name__ == "__main__":
    main()
