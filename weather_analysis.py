
import requests
import pandas as pd

API_KEY = "58a3563ae9ea613240859825852c2c55"

cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]

weather_list = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    weather_list.append({
        "City": data["name"],
        "Temperature": data["main"]["temp"],
        "Humidity": data["main"]["humidity"],
        "Wind Speed": data["wind"]["speed"]
    })

df = pd.DataFrame(weather_list)

df.to_csv("weather_data.csv", index=False)

print(df)
print()
print(f"Hottest City: {df.loc[df['Temperature'].idxmax(), 'City']}")
print(f"Average Temperature: {df['Temperature'].mean():.2f}°C")
print(f"Highest Humidity City: {df.loc[df['Humidity'].idxmax(), 'City']}")