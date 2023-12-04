import smtplib
import pandas as pd
from datetime import datetime
import random

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
date_now = datetime.now()
birthday_data = pd.read_csv("birthdays.csv")

for idx, row in birthday_data.iterrows():
    if date_now.month == row["month"] and date_now.day == row["day"]:
        my_email = "XXXXXX@gmail.com"
        password = "XXXXXXXXXXXXXXXX"
        letter = random.choice(letters)
        with open(f"letter_templates/{letter}") as file:
            file_read = file.read()
            final_letter = file_read.replace("[NAME]", f"{row["name"]}")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row.email,
                msg=f"Subject:Happy Birthday!\n\n{final_letter}"
            )
