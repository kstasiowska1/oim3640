import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from mbta_helper import get_coordinates, find_nearest_station

load_dotenv()

app = Flask(__name__)
MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=["POST"])
def search():
    place = request.form["place"]

    latitude, longitude = get_coordinates(place)

    if latitude is None or longitude is None:
        return render_template(
            "results.html",
            place=place,
            station="Location not found",
            map_urp=None
        )

    station = find_nearest_station(latitude, longitude)

    map_url = (
    f"https://api.mapbox.com/styles/v1/mapbox/streets-v12/static/"
    f"pin-s+ff0000({longitude},{latitude})/"
    f"{longitude},{latitude},14/600x400?access_token={MAPBOX_API_KEY}"
)

    return render_template(
        "results.html", 
        place=place, 
        station=station,
        map_url=map_url
        )

if __name__ == "__main__":
    app.run(debug=True)