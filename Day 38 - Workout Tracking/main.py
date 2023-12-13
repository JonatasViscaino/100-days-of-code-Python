import requests
from datetime import datetime

# EXERCISE PARAMETERS AND API NUTRITIONIX USE
APP_ID = "YOUR_ID"
API_KEY = "YOUR_KEY"
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

auth_params = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Tell me which exercises you did: ")

body_params = {
    "query": exercise_text,
    "gender": "YOUR_GENDER",
    "weight_kg": "YOUR_KG",
    "height_cm": "YOUR_HEIGHT",
    "age": "YOUR_AGE",
}

response = requests.post(url=NUTRI_ENDPOINT, headers=auth_params, json=body_params)
response.raise_for_status()
data = response.json()["exercises"]

# GOOGLE SHEETS PARAMETERS AND API SHEETY USE
for exercise in data:
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().time().strftime("%H:%M:%S")

    sheet_url = "YOUR SHEET URL"

    sheet_headers = {
        "Authorization": "Bearer YOUR_BEARER_ID",
    }

    sheet_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(sheet_url, headers=sheet_headers, json=sheet_body)
    sheet_response.raise_for_status()
    print(sheet_response.text)
