import requests


LATITUDE = 9.081999
LONGITUDE = 8.675277
API_KEY = "640861f597c635cd20f1c2145193486e"

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
