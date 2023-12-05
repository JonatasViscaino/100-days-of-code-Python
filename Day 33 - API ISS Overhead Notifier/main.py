import requests
from datetime import datetime
import smtplib
import time

# Constants
MY_LAT = 50.110924
MY_LONG = 8.682127
MY_EMAIL = "XXXXXX@gmail.com"
PASSWORD = "XXXXXXXXXXXXXXXX"


def is_iss_overhead():
    # Getting data from ISS API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    # Getting Data from Sunrise/Sunset API
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"][11:13])
    sunset = int(data["results"]["sunset"][11:13])

    hour_now = datetime.now().hour

    if hour_now <= sunrise or hour_now >= sunset:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky."
            )
