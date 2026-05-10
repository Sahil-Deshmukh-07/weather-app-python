import requests

API_KEY = "YOUR_API_KEY"
Base_URL = "http://api.openweathermap.org/data/2.5/weather"
result = ""

def get_weather(city:str):

    params = {
        "q" : city,
        "appid" : API_KEY,
        "units" : "metric"
    }

    response = requests.get(Base_URL, params = params)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        result = f"City: {city.capitalize()}\nTemp: {main['temp']}*C\nFeels like: {main['feels_like']}*C\nHumidity: {main['humidity']}\nWeather: {weather['description'].capitalize()}"

    else:
        result = "City not found"
    
    return result

