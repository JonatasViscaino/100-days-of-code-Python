# Day 32 - Automated Birthday Wisher

This Python script automatically sends birthday emails based on data provided in a CSV file. It reads birthdays from the "birthdays.csv" file, checks if any birthdays match the current date, and sends a personalized email using one of the randomly selected letter templates.

## Setup:

1. Add your Gmail credentials and customize the letter templates:
- Open the script in a text editor.
- Replace "**XXXXXX@gmail.com**" and "**XXXXXXXXXXXXXXXX**" with your Gmail email and app password.
- Customize the letter templates in the "letter_templates" directory.
2. Prepare the birthday data:
Create a CSV file named "birthdays.csv" with the following columns: "**name**", "**month**", "**year**", "**day**", "email".

The script will check for any birthdays on the current date and send personalized emails to the respective individuals.

## Notes:

- Ensure your Gmail account allows "Less secure app access" or use an "App password" if two-factor authentication is enabled.
- Make sure the letter templates in the "letter_templates" directory contain the placeholder "**[NAME]**" for the recipient's name.

Feel free to customize this template further based on your specific project details and requirements!