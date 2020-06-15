import requests, json, config
from twilio.rest import Client

zip_code = 10017
us_country_code = "us"
url = f"http://api.openweathermap.org/data/2.5/forecast?zip={zip_code},{us_country_code}&appid={config.WEATHER_API_KEY}"

def rain_is_possible(forcast_list):
    for forcast in forcast_list:
        if forcast['weather'][0]['main'] == 'Rain':
            return True
    return False


def send_alert_message():
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
    message_body = f"There is a chance of rain today. Make sure you're prepared!"
    client.messages.create(body=message_body,from_='+12053464547',to='+19092476022')


response = requests.get(url)
response_json_obj = response.json() 

if response_json_obj['cod'] == 401:
    print(f"Error making call to Weather API: {response_json_obj}")
else:
    forcast_list = response_json_obj['list']
    if rain_is_possible(forcast_list):
        send_alert_message()

