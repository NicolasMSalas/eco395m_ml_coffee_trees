import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Define the list of locations with latitude and longitude
locations = [
    {"name": "Brazil", "latitude": -17.9302, "longitude": -43.7908},
    {"name": "Vietnam", "latitude": 13.0635, "longitude": 108.2378},
    {"name": "Colombia", "latitude": 4.8121, "longitude": -75.6867},
]

# Loop over each location to fetch weather data and write to a separate CSV file
for location in locations:
    print(f"Fetching data for {location['name']}...")
    
    # Make the request for the current location
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "start_date": "1990-01-01",
        "end_date": "2025-03-08",
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "apparent_temperature_max", "apparent_temperature_min", "apparent_temperature_mean", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "precipitation_sum", "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant", "shortwave_radiation_sum", "et0_fao_evapotranspiration"]
    }
    responses = openmeteo.weather_api(url, params=params)
    
    # Process first location's data
    response = responses[0]
    
    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(2).ValuesAsNumpy()
    daily_temperature_2m_mean = daily.Variables(3).ValuesAsNumpy()
    daily_apparent_temperature_max = daily.Variables(4).ValuesAsNumpy()
    daily_apparent_temperature_min = daily.Variables(5).ValuesAsNumpy()
    daily_apparent_temperature_mean = daily.Variables(6).ValuesAsNumpy()
    daily_sunrise = daily.Variables(7).ValuesAsNumpy()
    daily_sunset = daily.Variables(8).ValuesAsNumpy()
    daily_daylight_duration = daily.Variables(9).ValuesAsNumpy()
    daily_sunshine_duration = daily.Variables(10).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(11).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(12).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(13).ValuesAsNumpy()
    daily_precipitation_hours = daily.Variables(14).ValuesAsNumpy()
    daily_wind_speed_10m_max = daily.Variables(15).ValuesAsNumpy()
    daily_wind_gusts_10m_max = daily.Variables(16).ValuesAsNumpy()
    daily_wind_direction_10m_dominant = daily.Variables(17).ValuesAsNumpy()
    daily_shortwave_radiation_sum = daily.Variables(18).ValuesAsNumpy()
    daily_et0_fao_evapotranspiration = daily.Variables(19).ValuesAsNumpy()

    # Create a dictionary to hold the data
    daily_data = {
        "location": location["name"],
        "date": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
            end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        ),
        "weather_code": daily_weather_code,
        "temperature_2m_max": daily_temperature_2m_max,
        "temperature_2m_min": daily_temperature_2m_min,
        "temperature_2m_mean": daily_temperature_2m_mean,
        "apparent_temperature_max": daily_apparent_temperature_max,
        "apparent_temperature_min": daily_apparent_temperature_min,
        "apparent_temperature_mean": daily_apparent_temperature_mean,
        "sunrise": daily_sunrise,
        "sunset": daily_sunset,
        "daylight_duration": daily_daylight_duration,
        "sunshine_duration": daily_sunshine_duration,
        "precipitation_sum": daily_precipitation_sum,
        "rain_sum": daily_rain_sum,
        "snowfall_sum": daily_snowfall_sum,
        "precipitation_hours": daily_precipitation_hours,
        "wind_speed_10m_max": daily_wind_speed_10m_max,
        "wind_gusts_10m_max": daily_wind_gusts_10m_max,
        "wind_direction_10m_dominant": daily_wind_direction_10m_dominant,
        "shortwave_radiation_sum": daily_shortwave_radiation_sum,
        "et0_fao_evapotranspiration": daily_et0_fao_evapotranspiration
    }


    daily_dataframe = pd.DataFrame(data=daily_data)
    
    file_path = f"data/weather_data_{location['name']}.csv"
    daily_dataframe.to_csv(file_path, index=False)
    
