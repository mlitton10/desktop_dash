import requests
import json
from interface.utils import get_lat_long


class BaseRequest:
    def __init__(self, url):
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        self.data = response.json()
        pass


class WeatherRequest(BaseRequest):
    def __init__(self, coords, n_days=7):
        api_key = "e5d294f92b8b38cad7c5252af8b68a20"

        api_string = "http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&cnt={}&appid={}".format(coords[0], coords[1], n_days, api_key)

        super().__init__(api_string)

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


if __name__=="__main__":
    w = WeatherRequestManager()
    print(w.data_dict)
