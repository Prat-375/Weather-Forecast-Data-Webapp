from dotenv import load_dotenv
import os
import requests

load_dotenv()
openweather_api_key = os.getenv("OPENWEATHER_API_KEY")

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={openweather_api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        filtered_data = data["list"]
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]
        return filtered_data
    else:
        return []

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3))