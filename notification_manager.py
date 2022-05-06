from twilio.rest import Client
import smtplib
import requests
my_email = "riteshlade28@gmail.com"
password = "@RSL281222"
TWILIO_ID = "ACa995ecc351535a8cd1d4e4bdec101b31"
TWILIO_TOKEN = "e891c976a9480bc355761287d1d89c12"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/e629599160fc8fdcc5c5e66da4b778ae/flightDeals/users"

class NotificationManager:


    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self,message):
        client = Client(TWILIO_ID, TWILIO_TOKEN)

        message = client.messages \
            .create(
            body=message,
            from_='+19034377244',
            to='+91 8421577093'
        )

    def send_emails(self,message, google_link):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        print(f'Message has sent to {data["users"][0]["email"]}')
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)

            for user in data["users"]:
                connection.sendmail(from_addr=my_email, to_addrs=user["email"],
                                    msg=f"Subject:Low Price Alert!\n\n{message}{google_link}".encode('utf-8'))

