import requests, os

class ExternalBookApiClient:
    BASE_URL = os.getenv('NY_TIMES_BOOKS_API_URL')
    API_KEY = os.getenv('NY_TIMES_BOOKS_API_KEY')

    def get(self, endpoint: str) -> dict:
        url = self.BASE_URL + endpoint

        params = {'api-key': self.API_KEY}

        response = requests.get(url, params)

        response.raise_for_status()

        return response.json()
