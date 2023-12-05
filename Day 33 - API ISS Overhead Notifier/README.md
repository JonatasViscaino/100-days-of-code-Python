# Day 33 - API ISS Overhead Notifier

This Python script leverages two APIs to provide real-time information about the International Space Station (ISS) and the local sunrise/sunset times and demonstrates the use of HTTP requests, and basic automation for space enthusiasts and those interested in celestial observations.  
If the ISS is currently overhead within a specified geographical location, and it is nighttime, the script sends an email notification.  

## Key Features:

- Utilizes the Open Notify API to fetch the current position of the ISS.
- Uses the Sunrise/Sunset API to retrieve local sunrise and sunset times.
- Periodically checks if the ISS is overhead and if it is currently nighttime.
- Sends email notifications using the Gmail SMTP server when both conditions are met.

## How to Use:

1. Set your location coordinates (**MY_LAT** and **MY_LONG**) and email credentials (**MY_EMAIL** and **PASSWORD**).
2. Run the script, and it will continuously monitor the ISS position and local time.
3. Receive email notifications when the ISS is overhead during nighttime.

This project showcases practical applications of API integration, real-time data retrieval, and basic automation for space-related observations. It serves as a valuable tool for enthusiasts keen on tracking the ISS movements and enjoying the beauty of the night sky.

Feel free to customize this description based on additional features or aspects you find noteworthy in your project.
