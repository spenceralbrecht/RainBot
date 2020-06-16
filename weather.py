import requests, json, os
MY_HOME_LOCATION_KEY = "3712_PC"
BASE_URL = "http://dataservice.accuweather.com/"
SINGLE_DAY_FORCAST_ENDPOINT = "forecasts/v1/daily/1day/"
api_key_portion = f"?apikey={os.environ['ACCUWEATHER_API_KEY']}&details=true"
request_url = BASE_URL + SINGLE_DAY_FORCAST_ENDPOINT + MY_HOME_LOCATION_KEY + api_key_portion

def get_rain_data():
    response = requests.get(request_url)
    response_json_obj = response.json()
    rain_dict = {
        'rain_probability' : response_json_obj["DailyForecasts"][0]["Day"]["RainProbability"],
        'rain_in_inches' : response_json_obj["DailyForecasts"][0]["Day"]["Rain"]["Value"],
        'hours_of_rain' : response_json_obj["DailyForecasts"][0]["Day"]["HoursOfRain"]
    }
    return rain_dict


