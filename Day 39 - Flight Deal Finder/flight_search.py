import requests
from flight_data import FlightData

URL_TEQUILA_API = "https://api.tequila.kiwi.com"
API_KEY = "YOUR API KEY"


class FlightSearch:

    def get_destination_code(self, city_name):
        headers = {"apikey": API_KEY}
        query = {
            "term": city_name,
            "location_types": "airport"
        }
        response = requests.get(f"{URL_TEQUILA_API}/locations/query", headers=headers, params=query)
        data = response.json()
        location = data["locations"][0]["city"]["code"]
        return location

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(f"{URL_TEQUILA_API}/v2/search", headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: EUR {flight_data.price}")
        return flight_data
