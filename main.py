my_api =  "d5b5cf1812c576b41f715f60dace6b55"
import requests
from twilio.rest import *

MY_ACCOUNT_SID = "AC5446eb4b4ada70cc13d04a7534d5b49c"
MY_AUTH_TOKEN = "a718be83c808e2d995a2c9240763b8ea"

MY_LAT = -47.8952 # Your latitude
MY_LONG = 155.543 # Your longitude
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": my_api,
    "cnt": 4,
}
will_rain = False
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast?",params= weather_params)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
print (weather_data["list"][0]["weather"])
for hourly_data in weather_data["list"]:
    condition_data =  (hourly_data["weather"][0]["id"])
    if condition_data < 600:
        will_rain= True

if will_rain:
    client = Client(MY_ACCOUNT_SID, MY_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="take an umbrella its rainy☔",
        from_='+14243425567',
        to="+972538219974"
    )
    print(message.status)


