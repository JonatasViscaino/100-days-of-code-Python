from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# Origin Airport
ORIGIN_CITY_IATA = "YOUR_ORIGIN"

# Creating DataManager object and getting data
data_manager = DataManager()
sheet_data = data_manager.get_data()

# Creating FlightSearch object
flight_search = FlightSearch()

# Creating NotificationManager object
notification_manager = NotificationManager()

# Check if iataCode is not blank in google sheets
for data in sheet_data:
    if not data['iataCode']:
        location = flight_search.get_destination_code(data["city"])
        data['iataCode'] = location
        data_manager.update_destination_codes(data)

# Creating dates to make the search
today_date = datetime.today()
tomorrow_date = (today_date + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_date = (today_date + timedelta(days=180)).strftime("%d/%m/%Y")

# Searching flights
for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow_date,
        to_time=six_month_date,
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_email(
            message=f"Subject:Flight Alert {flight.origin_city}-{flight.destination_city}\n\nLow price alert! Only EUR {flight.price} to fly from {flight.origin_city}-{flight.origin_airport}"
                    f" to {flight.destination_city}-{flight.destination_airport},"
                    f" from {flight.out_date} to {flight.return_date}."
        )
