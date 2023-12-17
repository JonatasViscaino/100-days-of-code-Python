# Day 39 - Flight Deal Alert System

This Python script monitors flight prices and sends email alerts for potential travel deals based on user-defined criteria. It utilizes a combination of data management, flight search, and notification modules to automate the process.

## Components
1. **DataManager:** Manages data stored in Google Sheets, including destination information and corresponding IATA codes. If an IATA code is missing, it uses the FlightSearch module to retrieve and update the data.
2. **FlightSearch:** Interacts with Kiwi Partners Flight Search API to find available flights within a specified date range. It dynamically obtains IATA codes for destinations and checks for potential deals.
3. **NotificationManager:** Handles the notification process, currently supporting email alerts. Sends alerts when a flight deal meeting user criteria is detected.

## Usage
- Set the **ORIGIN_CITY_IATA** variable to your desired origin airport's IATA code.
- The script retrieves destination data from Google Sheets, updates missing IATA codes, and searches for flight deals within a specified timeframe (from tomorrow to six months ahead).
- If a flight with a price lower than the recorded lowest price for a destination is found, an email alert is sent via the NotificationManager.

## How to Use
1. Populate the Google Sheets with destination cities and their corresponding IATA codes. You can use this link as reference [Google Sheets](https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?usp=sharing).

2. Configure the origin airport's IATA code and API key of kiwi.
3. Set up email credentials for the NotificationManager to enable email alerts.
4. Run the script periodically to check for new flight deals.

## Dependencies
- **data_manager.py**: Manages data stored in Google Sheets.
- **flight_search.py**: Interacts with flight search APIs to find flight details.
- **notification_manager.py**: Handles notifications, currently supporting email alerts.
- **datetime**: Manages date and time information.

Feel free to customize this description according to additional details or specific functionalities in your code.
