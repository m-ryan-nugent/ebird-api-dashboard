import sys

print(sys.executable)

from unittest import TestCase, main
from unittest.mock import patch, MagicMock

from src.text_formatter import TextFormatter

import openai
import openai_responses


class TestTextFormatter(TestCase):

    def setUp(self):
        self.openai_api_key = "test_openai_api_key"
        self.formatter = TextFormatter(openai_api_key=self.openai_api_key)

    @openai_responses.mock()
    def test_get_species_descriptions(self, openai_mock):
        openai_mock.chat.completions.create.response = {
            "choices": [
                {
                    "index": 0,
                    "finish_reason": "stop",
                    "message": {
                        "content": "Test bird description",
                        "role": "assistant",
                    },
                }
            ]
        }

        species_list = ["American Robin", "House Sparrow"]

        expected_output = {
            "American Robin": "Test bird description",
            "House Sparrow": "Test bird description",
        }

        result = self.formatter.get_species_descriptions(
            species_list=species_list
        )

        self.assertEqual(result, expected_output)

    def test_get_species_descriptions_failure(self):
        species_list = ["American Robin", "House Sparrow"]

        descriptions = self.formatter.get_species_descriptions(
            species_list=species_list
        )

        for species in species_list:
            self.assertIn(
                "Error retrieving description", descriptions[species]
            )


if __name__ == "__main__":
    main()
