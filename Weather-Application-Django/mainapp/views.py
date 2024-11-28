from django.shortcuts import render
import requests  # for sending requests

# Create your views here.

def index(request):
    # Using Weather API - https://www.weatherapi.com/
    BASE_URL = 'http://api.weatherapi.com/v1'

    # Add your WeatherAPI key here
    API_KEY = 'd17ea432cc2c4b579d475629242811'  # Replace with your API key

    if request.method == 'POST':
        city = request.POST.get('city').lower()
        print(city)

        if API_KEY == 'paste-your-api-key':
            print('Please add your generated API key into the "API_KEY" variable within the views.py')
            return render(request, 'index.html', {'checker': 'Please add your generated API key into the "API_KEY" variable within the views.py'})

        elif city == '':
            print('No value')
            return render(request, 'index.html', {'checker': 'Please enter valid info...!'})

        else:
            request_url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}&aqi=yes"  # Enable air quality index (aqi=yes)

            response = requests.get(request_url)

            if response.status_code == 200:
                data = response.json()
                location = data['location']
                weather = data['current']
                air_quality = weather.get('air_quality', {})  # Air quality data

                # Extracting season based on the current month (simple logic for demonstration)
                month = int(location['localtime'].split('-')[1])
                if month in [12, 1, 2]:
                    season = 'Winter'
                elif month in [3, 4, 5]:
                    season = 'Spring'
                elif month in [6, 7, 8]:
                    season = 'Summer'
                else:
                    season = 'Autumn'

                context = {
                    'weather': weather['temp_c'],
                    'city_name': location['name'],
                    'region': location['region'],
                    'country': location['country'],
                    'lat': location['lat'],
                    'lon': location['lon'],
                    'localtime': location['localtime'],
                    'continent': location['tz_id'],
                    'humidity': weather['humidity'],  # Humidity in %
                    'wind_speed': weather['wind_kph'],  # Wind speed in km/h
                    'precipitation': weather['precip_mm'],  # Precipitation in mm
                    'season': season,  # Determined based on the month
                    'air_quality': {
                        'pm2_5': air_quality.get('pm2_5', 'N/A'),
                        'pm10': air_quality.get('pm10', 'N/A'),
                        'co': air_quality.get('co', 'N/A'),
                        'no2': air_quality.get('no2', 'N/A'),
                        'so2': air_quality.get('so2', 'N/A'),
                        'o3': air_quality.get('o3', 'N/A'),
                    },
                    'static_city': city
                }

                return render(request, 'index.html', context)

            else:
                print("An error occurred")
                return render(request, 'index.html', {'static_city': city, 'checker': 'Please enter a valid city'})

    return render(request, 'index.html', {})
