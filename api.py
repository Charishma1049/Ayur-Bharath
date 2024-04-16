import requests
from datetime import datetime

user_api = '52229d85776d0cce966ff1bd6903cc68'
location = input("Enter the city name: ")

complete_api_link = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={user_api}"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# Check if the API request was successful (status code 200)
if api_link.status_code == 200:
    # Extract the list of forecast entries
    forecast_list = api_data.get('list', [])

    # Display weather details for the next 30 entries
    for forecast in forecast_list[:30]:
        # Extract relevant information for each forecast
        date_time_str = forecast['dt_txt']
        date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
        temp_city = forecast['main']['temp'] - 273.15
        hmdt = forecast['main']['humidity']
        wind_spd = forecast['wind']['speed']
        pres = forecast['main']['pressure']

        # Display weather details for each forecast
        print("-------------------------------------------------------------")
        print("Weather Stats for - {} || {}".format(location.upper(), date_time.strftime("%d %b %Y | %I:%M:%S %p")))
        print("-------------------------------------------------------------")
        print("Temperature: {:.2f} deg C".format(temp_city))
        print("Pressure: {} hPa".format(pres))
        print("Humidity: {}%".format(hmdt))
        print("Wind Speed: {} kmph".format(wind_spd))
else:
    print(f"Failed to retrieve data. Status code: {api_link.status_code}")


