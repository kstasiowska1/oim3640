import os
import requests
from dotenv import load_dotenv

load_dotenv()
MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")


def get_coordinates(place):
    """
    Takes a place name and uses the Mapbox API to return its latitude and longitude.
    I keep this in a helper file so the API logic stays separate from the Flask routes.
    """
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{place}.json"
    params = {
        "access_token": MAPBOX_API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "features" in data and len(data["features"]) > 0:
        coordinates = data["features"][0]["center"]
        longitude = coordinates[0]
        latitude = coordinates[1]
        return latitude, longitude
    else:
        return None, None


def find_nearest_station(latitude, longitude):
    """
    Takes latitude and longitude and uses the MBTA API to find the nearest station.
    It returns the station name so the Flask app can display it on the results page.
    """
    url = "https://api-V3.mbta.com/stops"
    
    headers = {
        "x-api-key": MBTA_API_KEY}

    params = {
        "api_key": MBTA_API_KEY,
        "lat": latitude,
        "lon": longitude
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    
    if "data" in data and len(data["data"]) > 0:
        station_name = data["data"][0]["attributes"]["name"]
        return station_name
    else:
        return "No stations found nearby."