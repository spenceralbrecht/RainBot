import requests, json, config
from twilio.rest import Client

zip_code = 10017
us_country_code = "us"
url = f"https://api.openweathermap.org/data/2.5/forecast/hourly?zip={zip_code},{us_country_code}&appid={config.WEATHER_API_KEY}"
MIN_CHANCE_OF_RAIN_THRESHOLD = 0.25

response = requests.get(url)
response_json_obj = response.json() 

print(response_json_obj)

chance_of_rain = get_probability_precipitation(response_json_obj)

if chance_of_rain > MIN_CHANCE_OF_RAIN_THRESHOLD:
    # send_alert_message(chance_of_rain)
    pass

def get_probability_precipitation(response_json_obj):
    # check for rain
    pass

def send_alert_message(probability):
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
    message_body = f"There is a {probability*100}% chance of rain today. Make sure you're prepared!"
    client.messages.create(body=message_body,from_='+12053464547',to='+19092476022')
