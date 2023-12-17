import smtplib
from email.message import EmailMessage

MY_EMAIL = "jonatasmviscaino@gmail.com"
GMAIL_PASS = "kobkgwwxebfzgoqw"


class NotificationManager:

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as self.connection:
            self.connection.starttls()
            self.connection.login(user=MY_EMAIL, password=GMAIL_PASS)
            self.connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=message
            )
        return print("e-mail sent.")