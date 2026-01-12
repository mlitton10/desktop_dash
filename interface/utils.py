import tkinter as tk
from geopy.geocoders import Nominatim
from datetime import datetime
from pytz import timezone
import pytz

address_dict = {"My Home": "807 N Hudson Avenue, Los Angeles, California, United States",
                "Cait's Home": "11 S Termino Avenue, Long Beach California United States",
                "Work": "1000 Veteran Ave, Los Angeles, CA 90024"}


def get_lat_long(addresses):
    geolocator = Nominatim(user_agent='your_app_name')
    coordinates = {}

    for loc, address in addresses.items():
        location = geolocator.geocode(address)

        lat, lon = location.latitude, location.longitude

        coordinates[loc] = (lat, lon)
    return coordinates


def get_screen_size():
    root = tk.Tk()
    # set the window to be transparent or "iconic" to avoid it flashing on screen
    root.attributes('-alpha', 0)
    # Alternatively, you can use root.state('iconic') for a similar effect

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.destroy()  # Close the small Tkinter window that was created
    return screen_width, screen_height


def handle_timestamp(timestamp):
    LosAngeles = timezone('America/Los_Angeles')

    utc_aware = datetime.fromtimestamp(timestamp, tz=pytz.UTC)
    local_timezone = LosAngeles.normalize(utc_aware)

    return local_timezone.strftime('%Y-%m-%d %H:%M:%S')


if __name__ == "__main__":
    coords = get_lat_long(address_dict)
    print(coords)
