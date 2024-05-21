import requests
import matplotlib.pyplot as plt

def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code} - {response.text}")
        return None

def visualize_weather(data):
    if data is None:
        print("No data to visualize")
        return
    
    try:
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        # Нова візуалізація: кругова діаграма
        labels = ['Temperature (°C)', 'Humidity (%)']
        values = [temp, humidity]
        colors = ['blue', 'green']
        
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f"Weather in {data['name']}: {description}")
        plt.show()

    except KeyError as e:
        print(f"Missing expected data in the API response: {e}")

# Введіть ваше місто і API ключ
city = "Kiev"
api_key = "f6dfe155d2878d356f1f2cdedf79bcbd"

# Отримання даних про погоду
weather_data = get_weather(city, api_key)

# Візуалізація даних про погоду
visualize_weather(weather_data)


