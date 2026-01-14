import requests
import json
from interface.utils import get_lat_long
import pandas as pd

class BaseRequest:
    def __init__(self, url, app_name):
        api_key = self._collect_keys(app_name)
        print(url.format(api_key))
        response = requests.get(url.format({api_key}))
        print(f"Status Code: {response.status_code}")

        self.data = response.json()
        pass

    def _collect_keys(self, app_name):
        keys_df = pd.read_csv('../keys.txt')
        key_dict = {name: key for name, key in zip(keys_df['API'], keys_df['key'])}
        return key_dict[app_name]



class WeatherRequest(BaseRequest):
    def __init__(self, coords, n_days=7):

        api_string = "http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&cnt={}&appid={{}}".format(coords[0], coords[1], n_days)

        super().__init__(api_string, 'open_weather')

class WeatherRequestManager():
    def __init__(self):
        address_dict = {"My Home": "807 N Hudson Avenue, Los Angeles, California, United States",
                        "Cait's Home": "11 S Termino Avenue, Long Beach California United States",
                        "Work": "1000 Veteran Ave, Los Angeles, CA 90024"}

        coords = get_lat_long(address_dict)
        self.data_dict = {}
        for location, coord in coords.items():
            weather = WeatherRequest(coord)
            self.data_dict[location] = weather.data

    def _format_json_data(self):
        clean_data = {}
        for location, data in self.data_dict.items():
            clean_data[location] = data['list']


if __name__=="__main__":
    w = WeatherRequestManager()
    print(w.data_dict)
