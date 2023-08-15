import requests

user_input = input("Введіть координати в десяткових градусах через кому, приклад: 49.хххх, 24.хххх\n")
input_list = user_input.split(",")
if len(input_list) != 2:
    print("\nневірний формат вводу")
    exit(1)

latitude_longitude_dictionary = {"latitude": input_list[0], "longitude": input_list[1]}


def validate_and_execute(latitude_longitude_dictionary):
    try:
        user_input_latitude = float(latitude_longitude_dictionary["latitude"])
        user_input_longitude = float(latitude_longitude_dictionary["longitude"])
    except ValueError:
        print("невірний формат вводу")
        exit(1)


validate_and_execute(latitude_longitude_dictionary)

input_latitude = float(latitude_longitude_dictionary["latitude"])
input_longitude = float(latitude_longitude_dictionary["longitude"])


response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={input_latitude}&longitude={input_longitude}&hourly=temperature_2m&current_weather=true&temperature_unit=celsius&windspeed_unit=ms&timezone=auto")
API_data = response.json()
weather_value = API_data['current_weather']

print(type(weather_value))
print(weather_value)


