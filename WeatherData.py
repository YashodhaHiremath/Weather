import requests

API_KEY = '290f9a6d42d6d0389dd8d42b3e042a2c'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather_data(city_name):
    params = {'q': city_name, 'appid': API_KEY}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data


def get_temperature(date):
    city_name = input("Enter the city name: ")
    weather_data = get_weather_data(city_name)
    temp = weather_data['main']['temp']
    return temp


def get_wind_speed(date):
    city_name = input("Enter the city name: ")
    weather_data = get_weather_data(city_name)
    wind_speed = weather_data['wind']['speed']
    return wind_speed


def get_pressure(date):
    city_name = input("Enter the city name: ")
    weather_data = get_weather_data(city_name)
    pressure = weather_data['main']['pressure']
    return pressure


def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date: ")
            temperature = get_temperature(date)
            print(f"Temperature on {date}: {temperature} K")

        elif choice == 2:
            date = input("Enter the date: ")
            wind_speed = get_wind_speed(date)
            print(f"Wind Speed on {date}: {wind_speed} m/s")

        elif choice == 3:
            date = input("Enter the date: ")
            pressure = get_pressure(date)
            print(f"Pressure on {date}: {pressure} hPa")

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()