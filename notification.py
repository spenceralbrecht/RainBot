import config, os
from twilio.rest import Client


def send_alert_message(chance_of_rain):
    client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    message_body = f"There is a {chance_of_rain*100}% chance of rain today. Make sure you're prepared!"
    client.messages.create(body=message_body,from_='+12053464547',to='+19092476022')