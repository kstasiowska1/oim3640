from flask import Flask, render_template, request
from mbta_helper import get_corrdinates, find_nearest_station

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=["POST"])
def search():
    place = request.form["place"]

    latitude, longitude = get_coordinates(place)
    station = find_nearest_station((latitude, longitude))
    
    return render_template('results.html', place=place, station=station)

if __name__ == "__main__":
    app.run(debug=True)