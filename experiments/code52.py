def weather(temperature):
    if temperature > 25:
        return "Hot"
    elif temperature >= 15 and temperature <= 25:
        return "Warm"
    else:
        return "cold"

weather_forecast = weather(26)
print(weather_forecast)