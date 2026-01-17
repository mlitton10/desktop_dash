import requests
import json
from interface.utils import get_lat_long
import pandas as pd

class BaseRequest:
    def __init__(self, url):
        response = requests.get(url)
       # print(f"Status Code: {response.status_code}")

        self.data = response.json()
        pass

    def _collect_keys(self, app_name):
        keys_df = pd.read_csv('../keys.txt')
        key_dict = {name: key for name, key in zip(keys_df['API'], keys_df['key'])}
        return key_dict[app_name]



class WeatherRequest(BaseRequest):
    def __init__(self, coords, n_days=7):
        api_string = "https://api.weather.gov/points/{},{}".format(coords[0], coords[1])
        super().__init__(api_string)

class WeatherRequestManager():
    def __init__(self):
        address_dict = {"My Home": "807 N Hudson Avenue, Los Angeles, California, United States",
                        "Cait's Home": "11 S Termino Avenue, Long Beach California United States",
                        "Work": "1000 Veteran Ave, Los Angeles, CA 90024"}

        coords = get_lat_long(address_dict)
        self.weather_api_strings = {}
        for location, coord in coords.items():
            api_str_data = WeatherRequest(coord)
            self.weather_api_strings[location] = api_str_data.data['properties']['forecast']

        self.weather_data_json = {}
        self.weather_data = {}
        for location, string in self.weather_api_strings.items():
            api_data = BaseRequest(string)
            self.weather_data_json[location] = api_data.data
        self.weather_data = self._collect_weather_data()

    def _collect_weather_data(self):
        weather_data = {}
        for location, data in self.weather_data_json.items():
            temp = data['properties']['periods'][0]['temperature']
            precip = data['properties']['periods'][0]['probabilityOfPrecipitation']['value']

            timing = data['properties']['periods'][0]['name']
            wind = data['properties']['periods'][0]['windSpeed']
            summary = data['properties']['periods'][0]['shortForecast']

            data_dict = {'timing': timing, 'temp': temp, 'precip': precip, 'wind': wind, 'summary':summary}
            weather_data[location] = data_dict
        return weather_data


if __name__=="__main__":
    w = WeatherRequestManager()
    print(w.weather_data)
