import requests


class EBirdDataFetcher:
    BASE_URL = "https://api.ebird.org/v2"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"X-eBirdApiToken": self.api_key}

    def get_recent_observations(self, region_code):
        endpoint = f"{self.BASE_URL}/data/obs/{region_code}/recent"
        response = requests.get(endpoint, headers=self.headers)

        return response.json() if response.status_code == 200 else None
