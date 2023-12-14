import requests

SHEETY_ENDPOINT = "https://api.sheety.co/c307d28896553a130d44a6f082c0b557/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.data = {}

    def get_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.data = data["prices"]
        return self.data

    def update_destination_codes(self, data):
        new_data = {
            "price": {
                "iataCode": data["iataCode"]
            }
        }
        response = requests.put(f"{SHEETY_ENDPOINT}/{data['id']}", json=new_data)
        response.raise_for_status()
        print(response.text)
