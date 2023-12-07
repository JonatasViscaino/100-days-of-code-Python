# Day 35 - Weather Alert System by SMS

## Overview:
This Python script utilizes the OpenWeatherMap API to check the upcoming weather forecast for a specified location. It determines whether it's going to rain within the next few hours by analyzing the weather condition codes. If rain is expected, the script sends an SMS alert using the Twilio API to a predefined phone number. The user needs to provide their OpenWeatherMap API key, Twilio account SID, auth token, and relevant phone numbers.

## Usage:
1. Obtain API keys from OpenWeatherMap and Twilio.
2. Set the latitude and longitude coordinates for the current location (MY_LAT, MY_LON).
3. Configure the Twilio account SID, auth token, and phone numbers (to and from_).
4. Run the script to receive an SMS alert if rain is forecasted.

**Note:** Ensure that you have the required Python packages installed by running:

```bash
pip install requests twilio
```
Make sure to replace placeholders like "XXXXX" with the actual API keys, phone numbers, and other specific information. Additionally, include any additional setup or configuration instructions that might be helpful for users who want to use or contribute to your code.

Feel free to customize the script and adapt it to your specific needs.