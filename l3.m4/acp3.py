import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current=temperature_2m,relative_humidity_2m,wind_speed_10m"

def weather():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\nCurrent Weather")
        print("Timezone:", data["timezone"])
        print("Temperature:", data["current"]["temperature_2m"], "°C")
        print("Humidity:", data["current"]["relative_humidity_2m"], "%")
        print("Wind Speed:", data["current"]["wind_speed_10m"], "km/h")
    else:
        print("Unable to fetch weather.")

while True:
    s = input("\nPress Enter to get weather or type 'Q' to quit: ")

    if s.upper() == "Q":
        break

    weather()