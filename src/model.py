import requests


class OpenSkyApi:
    BASE_URL = "https://opensky-network.org/api/"

    def fetch_all_states(self):
        url = self.BASE_URL + "states/all"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["states"]
        else:
            return None
