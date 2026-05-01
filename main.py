# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import requests
import os
from twilio.rest import Client
MY_LAT = 26.735729#60.169857
MY_LONG = 85.928291#24.938379
timestamp_count = 4
api_key = os.environ.get("OWM_API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "cnt": timestamp_count,
        "appid": api_key,
    }

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for timestamp in weather_data["list"]:
    if timestamp["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella. ☂️☂️☂️☂️",
        to="whatsapp:358406788102"
    )
    print(message.status)
