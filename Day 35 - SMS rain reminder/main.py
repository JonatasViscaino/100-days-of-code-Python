import requests
from twilio.rest import Client

account_sid = "XXXXXX"
auth_token = "XXXXX"

API_KEY = "XXXXX"
MY_LAT = 50.110924
MY_LON = 8.682127

parameteres = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameteres)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for weather in weather_data["list"]:
    condition_code = weather["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring an ☔️",
        to="XXXXX", from_="XXXXX"
    )
    print(message.status)
