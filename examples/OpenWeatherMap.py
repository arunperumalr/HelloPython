import requests

API_KEY = "0b0c21fb479069c9564f980121c5764c"
CITY = "Chennai"
BASE_URL =  "https://api.openweathermap.org/data/2.5/weather"


weather_url = f"{BASE_URL}?q={CITY}&APPID={API_KEY}"

print("Updated Weather URL: ",weather_url)

weather_response = requests.get(weather_url)
print("Status_Code: ", weather_response.status_code)

if weather_response.status_code == 200:
    weather_data = weather_response.json()

    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    print("\nWeather Report for City : ", CITY)
    print("*" * 27)
    print("Temperature: ", temperature)
    print("Humidity: ", humidity)
    print("Description: ", description)
    print("-" * 40)

else:
    print("No weather data found")
