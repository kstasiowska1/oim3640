from flask import Flask, render_template, request
from mbta_helper import get_coordinates, find_nearest_station

app = Flask(__name__)

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
            station="Location not found"
        )

    station = find_nearest_station(latitude, longitude)

    return render_template("results.html", place=place, station=station)

if __name__ == "__main__":
    app.run(debug=True)