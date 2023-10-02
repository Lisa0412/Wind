import requests
#from weathercode_dictionary import weathercode_dictionary_codes

#user_input = input("Введіть координати в десяткових градусах через кому, приклад: 49.хххх, 24.хххх\n")
#input_list = user_input.split(",")
#if len(input_list) != 2:
 #   print("\nневірний формат вводу")
 #   exit(1)

#latitude_longitude_dictionary = {"latitude": input_list[0], "longitude": input_list[1]}


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

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={input_latitude}&longitude={input_longitude}&current_weather=true&temperature_unit=celsius&windspeed_unit=ms&timezone=auto&hourly=windspeed_120m")
API_data = response.json()
weather_value = API_data['current_weather']
#weather_value_detailed = API_data['hourly']
#апі респонз змінна is_day дорівнює 1 коли в знайденому регіоні день і 0 коли ніч

#print(weather_value)
#print(weather_value_detailed)

weathercode_dictionary_codes = {"0": "Ясно",
                          "1": "Переважно ясно",
                          "2": "Частково хмарно",
                          "3": "Хмарно",
                          "45": "Туман",
                          "48": "Туман, іней",
                          "51": "Слабка мряка",
                          "53": "Помірна мряка",
                          "55": "Сильна мряка",
                          "56": "Крижаний дощ (невисока інтенсивність)",
                          "57": "Крижаний дощ",
                          "61": "Слабкий дощ",
                          "63": "Дощ",
                          "65": "Злива",
                          "66": "Крижаний дощ",
                          "67": "Крижана злива",
                          "71": "Снігопад (легкий)",
                          "73": "Снігопад (помірний)",
                          "75": "Снігопад (сильний)",
                          "77": "Град",
                          "80": "Злива",
                          "81": "Злива",
                          "82": "Злива",
                          "85": "Злива",
                          "86": "Злива",
                          "95": "Гроза",
                          "96": "Гроза",
                          "99": "Гроза",
                          }


print(" Погода: ", weathercode_dictionary_codes[str(weather_value['weathercode'])], "\n"
      " Температура повітря: ", weather_value['temperature'], "°C\n",
      "Середня швидкість вітру: ", weather_value['windspeed'], "м/с\n",
      "Напрям вітру: ", weather_value['winddirection'], "°\n"
      " Дата і час, коли зроблений прогноз: ", weather_value['time'], "\n"
      )


